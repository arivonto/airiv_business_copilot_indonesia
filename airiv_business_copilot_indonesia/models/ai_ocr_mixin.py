# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AirivAiOcrMixin(models.AbstractModel):
    _name = 'airiv.ai.ocr.mixin'
    _description = 'Mixin Ekstraksi Dokumen Cerdas'

    ai_extracted = fields.Boolean(string="Diekstraksi AI", default=False, readonly=True)
    ai_confidence_score = fields.Float(string="Skor Akurasi AI", default=0.98, readonly=True)
