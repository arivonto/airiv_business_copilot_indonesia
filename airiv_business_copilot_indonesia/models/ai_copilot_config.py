# -*- coding: utf-8 -*-
import json
import logging
import urllib.request
import urllib.error
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

class AirivAiCopilotConfig(models.Model):
    _name = 'airiv.ai.copilot.config'
    _description = 'Konfigurasi Google Gemini AI Copilot'
    _rec_name = 'name'

    name = fields.Char(string="Nama Integrasi", default="Google Gemini 2.5 Flash Engine", required=True)
    company_id = fields.Many2one('res.company', string="Perusahaan", default=lambda self: self.env.company, required=True)

    environment = fields.Selection([
        ('mock', 'Offline Mock Simulation (0 Akun / Tanpa API Key)'),
        ('ai_studio', 'Google AI Studio (Gemini 2.5 Flash Free Tier)'),
        ('vertex_ai', 'Google Cloud Vertex AI (Enterprise)'),
    ], string="Mode Eksekusi AI", default='mock', required=True)

    gemini_api_key = fields.Char(string="Gemini API Key", help="Dapatkan gratis di Google AI Studio (aistudio.google.com)")
    model_version = fields.Selection([
        ('gemini-2.5-flash', 'Gemini 2.5 Flash (Tercepat & Rekomendasi UMKM)'),
        ('gemini-2.5-pro', 'Gemini 2.5 Pro (Analisis Kompleks)'),
    ], string="Versi Model", default='gemini-2.5-flash', required=True)

    temperature = fields.Float(string="Kreativitas (Temperature)", default=0.2, help="0.0 - 0.3 untuk akurasi OCR / Data Medis")

    @api.model
    def get_active_config(self):
        cfg = self.search([('company_id', '=', self.env.company.id)], limit=1)
        if not cfg:
            cfg = self.create({'company_id': self.env.company.id})
        return cfg

    def generate_ai_response(self, system_prompt, user_content, response_format='text'):
        self.ensure_one()
        if self.environment == 'mock':
            # Deterministic Offline Simulator
            return self._mock_router(system_prompt, user_content, response_format)

        # Live Google AI Studio REST Engine (Zero SDK Overhead)
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_version}:generateContent?key={self.gemini_api_key}"
        payload = {
            "contents": [{"parts": [{"text": f"{system_prompt}\n\nUser Query / Input:\n{user_content}"}]}],
            "generationConfig": {
                "temperature": self.temperature,
            }
        }
        if response_format == 'json':
            payload["generationConfig"]["response_mime_type"] = "application/json"

        try:
            req = urllib.request.Request(
                endpoint,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                return result['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            _logger.error("[GEMINI REST ERROR] %s", e)
            return json.dumps({'error': str(e)}) if response_format == 'json' else f"Gagal menghubungi server Gemini: {e}"

    def _mock_router(self, system_prompt, user_content, response_format):
        # 1. OCR Vendor Bill Scenario
        if 'ocr' in system_prompt.lower() or 'invoice' in system_prompt.lower():
            mock_ocr = {
                "vendor_name": "PT Sumber Rejeki Abadi",
                "vendor_npwp": "0123456789012345",
                "invoice_number": "INV/2026/08/9981",
                "invoice_date": fields.Date.today().strftime('%Y-%m-%d'),
                "lines": [
                    {"product_name": "Kertas Thermal 80mm", "qty": 10, "price_unit": 25000.0, "subtotal": 250000.0},
                    {"product_name": "Tinta Struk Ribbon", "qty": 2, "price_unit": 75000.0, "subtotal": 150000.0}
                ],
                "dpp_subtotal": 400000.0,
                "ppn_12": 48000.0,
                "total_amount": 448000.0
            }
            return json.dumps(mock_ocr)

        # 2. Healthcare SOAP Scenario
        elif 'soap' in system_prompt.lower() or 'medis' in system_prompt.lower():
            mock_soap = {
                "subjective": "Pasien mengeluh sakit gigi geraham kanan bawah berdenyut sejak 2 hari lalu.",
                "objective": "Gigi 46 karies profunda oklusal, perkusi positif, sondasi nyeri.",
                "assessment_icd10": "K04.0",
                "assessment_diagnosis": "Pulpitis akut gigi 46",
                "plan": "Pro pulpektomi / perawatan saluran akar (PSA), analgesik asam mefenamat 500mg 3x1."
            }
            return json.dumps(mock_soap)

        # 3. Customer Service / WhatsApp Scenario
        elif 'whatsapp' in system_prompt.lower() or 'stok' in system_prompt.lower():
            return "Halo Kak! Terima kasih sudah menghubungi kami. Stok produk tersebut saat ini TERSEDIA dan siap kami kirimkan hari ini menggunakan kurir pilihan Anda. Apakah ada kebutuhan lain yang bisa kami bantu?"

        # 4. SAK EMKM Financial Analysis Scenario
        else:
            return "Berdasarkan analisis SAK EMKM, kinerja keuangan bisnis berada dalam kondisi sehat. Margin laba kotor tercapai stabil dengan likuiditas aset lancar mencukupi kewajiban jangka pendek."
