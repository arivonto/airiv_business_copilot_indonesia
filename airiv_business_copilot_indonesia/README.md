# Indonesia Complete Business Copilot & AI Automation Engine (Gemini AI)

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![AI Engine: Gemini 2.5 Flash](https://img.shields.io/badge/AI%20Engine-Google%20Gemini%202.5%20Flash-purple.svg)](https://aistudio.google.com)

A cross-sector enterprise Artificial Intelligence Copilot powered natively by **Google Gemini 2.5 Flash** for **Odoo 18.0 Community Edition**. Provides document OCR, customer engagement drafting, clinical SOAP records structuring, and executive financial insights without external middleware servers.

---

## Detailed Cross-Sector Capabilities

### 1. Finance & Accounting Intelligence
* **Document & Struk OCR**: Extracts line items, vendor names, and 16-digit NPWP/NIK from paper receipts and PDF invoices.
* **Statutory PPN 12% Auto-Split**: Automatically isolates DPP and 12% value-added tax into draft vendor bills.
* **SAK EMKM Financial Summaries**: Analyzes Laporan Laba Rugi and Neraca to produce executive performance narratives.

### 2. Healthcare & Clinical RME (Rekam Medis)
* **Audio & Text SOAP Structuring**: Transforms unstructured doctor anamnesis into structured SOAP notes (Subjective, Objective, Assessment, Plan).
* **ICD-10 Diagnostic Matching**: Maps clinical findings directly to standard WHO/Kemenkes ICD-10 codes (e.g., K04.0 Pulpitis, A09 Gastroenteritis).

### 3. Omnichannel Commerce & Customer Service
* **Context-Aware WhatsApp Assistant**: Generates contextual responses to customer inquiries referencing real-time warehouse inventory and order status.
* **Smart Quotation Drafter**: Converts natural language customer requests into draft sales orders.

### 4. 3-Tier AI Execution Rails
* **Mode 1: Offline Mock Simulation**: Zero-cost, zero-signup instant evaluation with deterministic outputs for local dev and testing.
* **Mode 2: Google AI Studio Direct API**: Direct HTTPS REST integration to Gemini 2.5 Flash using free tier quotas.
* **Mode 3: Vertex AI**: Enterprise GCP connectivity for high-volume corporate pipelines.

---

## Validated Commercial Benchmark (Multi-Sector Audit)

The AI Copilot was verified under live Odoo 18.0 Community conditions across all 7 operational phases:

1. **Accounting Vendor Bill OCR**: Processed receipt `faktur_pembelian_supplier_atk.pdf`, extracting vendor `PT Sumber Rejeki Abadi` (NPWP `0123456789012345`), DPP `Rp 400.000,00`, statutory PPN 12% `Rp 48.000,00`, and total bill `Rp 448.000,00`.
2. **Clinical SOAP Note Formulator**: Structured doctor consultation into clinical SOAP format with primary diagnosis **ICD-10 K04.0** (*Pulpitis akut gigi 46*) and planned root canal treatment.
3. **Commerce WhatsApp Copilot**: Drafted contextual inventory reply for Paracetamol 500mg availability.
4. **SAK EMKM Financial Summary**: Formulated executive narrative for SAK EMKM financial statements.

---

## Installation & Odoo Configuration Guide

1. **Deploy Module**:
   Place `airiv_business_copilot_indonesia` inside your Odoo `custom_addons` directory.

2. **Activate Module**:
   * Navigate to **Apps > Update Apps List**.
   * Search for `Indonesia Complete Business Copilot & AI Automation Engine` and click **Activate**.

3. **Configure AI Engine**:
   * Open **AI Copilot > Pengaturan AI**.
   * Default to **Offline Mock Simulation** for instant practice, or select **Google AI Studio** and enter your free Gemini API Key from [aistudio.google.com](https://aistudio.google.com).

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL & App Drawer compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `base`, `account`, `stock`, `sale`, `airiv_whatsapp_indonesia`, `airiv_clinic_indonesia`, `airiv_accounting_indonesia` |
| **AI Foundation Model** | Google Gemini 2.5 Flash / Pro (Direct REST API) |
| **Server Overhead** | Zero (Direct client/server streams, no middleman proxy) |
