# Indonesia Complete Business Copilot & AI Automation Engine

[![Odoo 18](https://img.shields.io/badge/Odoo-18.0-714B67)](https://www.odoo.com/) [![License LGPL-3](https://img.shields.io/badge/license-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html) [![AIRIV](https://img.shields.io/badge/AIRIV-Indonesia%20AI-0F766E)](https://airiv.id)

Cross-sector assistance for Indonesian Odoo operations: document OCR, business reply drafting, clinical SOAP structuring, and financial insight workflows. Generated results remain reviewable and traceable before application.

## Core Capabilities & Architecture

- Document OCR for vendor bills and receipts, including supplier, tax, and line-item extraction.
- Context-aware drafting for WhatsApp and Chatter conversations, order summaries, and invoice status questions.
- Clinical anamnesis assistance with SOAP structure and ICD-10 matching support.
- Offline Mock Simulation, Google AI Studio Direct API, and Google Cloud Vertex AI configuration surfaces.
- Interaction records preserve execution mode, status, prompt context, and generated output.

The module connects native Odoo accounting, sales, stock, AIRIV WhatsApp, AIRIV Clinic, AIRIV Accounting, and AIRIV OS Core context to configurable copilot workflows. Generated content is assistive and requires human review.

## Feature & Workflow Automation

1. Configure the permitted execution mode and model policy.
2. Select a document, conversation, or clinical note as source context.
3. Run OCR, drafting, or SOAP assistance.
4. Review and edit the traceable interaction result.
5. Apply approved output to the target Odoo workflow.

## Technical Specifications

- Odoo: `18.0.1.0.0`, Community Edition compatible
- License: LGPL-3
- Main models: `ai.copilot.config`, `ai.copilot.interaction`, `ai.document.ocr.wizard`
- Dependencies: `base`, `account`, `stock`, `sale`, `airiv_whatsapp_indonesia`, `airiv_clinic_indonesia`, `airiv_accounting_indonesia`, `airiv_os_core`
- Store assets: `static/description/icon.png`, `banner.png`, and fragment-safe `index.html`

## Installation Guidance

1. Clone branch `18.0` into an Odoo addons path.
2. Install the declared AIRIV and Odoo dependencies.
3. Restart Odoo, update the Apps list, and install the module.
4. Open Copilot Configuration and select the permitted execution mode.

## Configuration Checklist

- Confirm declared dependencies are installed.
- Use Offline Mock for demonstrations without provider credentials.
- Configure hosted provider modes only under organizational security policy.
- Review generated tax, clinical, and customer-facing content before applying it.
- Retain interaction records for traceability.

## Repository Layout

```text
airiv_business_copilot_indonesia/
  models/                 Copilot configuration and interaction models
  wizard/                 Document OCR wizard and views
  security/               Access control declarations
  views/                  Menus and model views
  static/description/     Apps Store icon, banner, and index fragment
  __manifest__.py         Odoo metadata and dependencies
```

## Contact Info

- Author: AIRIV
- Website: https://airiv.id
- GitHub: https://github.com/arivonto
- Repository: https://github.com/arivonto/airiv_business_copilot_indonesia
- Odoo series: `18.0`

## Quality Gate

`.github/scripts/validate_odoo_appstore.py` and GitHub Actions audit manifest metadata, required store assets, XML-safe description markup, repository hygiene, and module structure on branch `18.0`.
