# -*- coding: utf-8 -*-
{
    'name': 'Indonesia Complete Business Copilot & AI Automation Engine (Gemini AI)',
    'version': '18.0.1.0.0',
    'category': 'Productivity/AI',
    'summary': 'Multi-Sector AI Copilot: Vendor Bill OCR (PPN 12%), WhatsApp AI Drafter, Clinical SOAP Formulator, & SAK EMKM Insights',
    'description': """
Universal Indonesian Business AI Copilot powered by Google Gemini 2.5 Flash for Odoo 18 Community Edition.
Delivers cross-sector automation across Accounting, Commerce, Healthcare, and Operations:

1. Finance & Accounting:
   - Automated Vendor Bill & Paper Receipt OCR with line-item extraction
   - Automatic 16-digit NPWP/NIK identification & statutory PPN 12% tax separation
   - SAK EMKM Financial Narrative Generator (Laporan Laba Rugi & Posisi Keuangan)
2. Commerce & Customer Support:
   - Context-aware WhatsApp & Chatter auto-reply drafting referencing live stock balances
   - Natural language order & invoice status summary
3. Healthcare & Clinical RME:
   - Voice/text anamnesis structuring into standard SOAP format
   - Automated ICD-10 diagnostic code matching & prescription interaction safety checks
4. Flexible 3-Tier AI Execution Rails:
   - Mode 1: Offline Mock Simulation (0 signups required, instant local evaluation)
   - Mode 2: Google AI Studio Direct API (Generous Free Quota, zero middleware server)
   - Mode 3: Google Cloud Vertex AI (Enterprise Scalability)
5. Zero External Server Overhead - 100% Odoo 18 Community Native - Always Free ($0.00).
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'base',
        'account',
        'stock',
        'sale',
        'airiv_whatsapp_indonesia',
        'airiv_clinic_indonesia',
        'airiv_accounting_indonesia',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/ai_document_ocr_wizard_views.xml',
        'views/ai_copilot_config_views.xml',
        'views/ai_copilot_interaction_views.xml',
        'views/copilot_menu_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
