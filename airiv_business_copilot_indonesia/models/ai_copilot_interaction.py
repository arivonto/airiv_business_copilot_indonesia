# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AirivAiInteraction(models.Model):
    _name = 'airiv.ai.interaction'
    _description = 'Riwayat Interaksi & Log AI Copilot'
    _order = 'create_date desc'

    name = fields.Char(string="Judul Interaksi", required=True, default="Permintaan AI Copilot")
    domain_type = fields.Selection([
        ('accounting', 'Akuntansi & OCR Faktur'),
        ('whatsapp', 'WhatsApp & CRM Drafter'),
        ('healthcare', 'Rekam Medis & Diagnosa SOAP'),
        ('operations', 'Analisis Stok & Operasional'),
    ], string="Sektor Bisnis", required=True, default='accounting')

    prompt_input = fields.Text(string="Prompt / Input Data", required=True)
    response_output = fields.Text(string="Hasil Analisis AI", readonly=True)
    execution_mode = fields.Selection([
        ('mock', 'Simulasi Offline'),
        ('ai_studio', 'Google AI Studio Live'),
    ], string="Mode Eksekusi", default='mock')
