# -*- coding: utf-8 -*-
import json
import base64
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AirivAiDocumentOcrWizard(models.TransientModel):
    _name = 'airiv.ai.document.ocr.wizard'
    _description = 'Pemindai Dokumen & Struk Cerdas AI'

    document_file = fields.Binary(string="Unggah Foto Struk / PDF Faktur", required=True)
    file_name = fields.Char(string="Nama File")
    document_type = fields.Selection([
        ('vendor_bill', 'Faktur Pembelian / Struk Belanja (Vendor Bill)'),
        ('medical_soap', 'Anamnesis Suara / Catatan Medis Dokter (SOAP)'),
        ('customer_chat', 'Pesan WhatsApp / Keluhan Pelanggan'),
    ], string="Tipe Dokumen", default='vendor_bill', required=True)

    extracted_preview = fields.Text(string="Hasil Ekstraksi Cerdas", readonly=True)

    def action_execute_ai_analysis(self):
        self.ensure_one()
        config = self.env['airiv.ai.copilot.config'].get_active_config()
        
        if self.document_type == 'vendor_bill':
            system_prompt = "You are an expert Indonesian tax and accounting OCR parser. Extract invoice details into JSON with keys: vendor_name, vendor_npwp, invoice_number, invoice_date, lines (product_name, qty, price_unit, subtotal), dpp_subtotal, ppn_12, total_amount."
            res_raw = config.generate_ai_response(system_prompt, f"Document: {self.file_name}", response_format='json')
            self.extracted_preview = res_raw
            
            # Create Audit Log
            self.env['airiv.ai.interaction'].create({
                'name': f"OCR Faktur: {self.file_name or 'Dokumen'}",
                'domain_type': 'accounting',
                'prompt_input': f"File: {self.file_name}",
                'response_output': res_raw,
                'execution_mode': 'mock' if config.environment == 'mock' else 'ai_studio',
            })
            
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'airiv.ai.document.ocr.wizard',
                'res_id': self.id,
                'view_mode': 'form',
                'target': 'new',
            }

        elif self.document_type == 'medical_soap':
            system_prompt = "You are a clinical assistant for Indonesian clinics. Structure text into standard SOAP JSON with keys: subjective, objective, assessment_icd10, assessment_diagnosis, plan."
            res_raw = config.generate_ai_response(system_prompt, f"Catatan: {self.file_name}", response_format='json')
            self.extracted_preview = res_raw
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'airiv.ai.document.ocr.wizard',
                'res_id': self.id,
                'view_mode': 'form',
                'target': 'new',
            }
