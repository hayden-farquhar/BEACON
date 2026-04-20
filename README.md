# BEACON

**Bayesian Evidence-Adjusted Clinical Outbreak Navigator**

Clinical decision support for febrile returned travellers presenting to Australian emergency departments.

[Live App](https://beacon-fever.streamlit.app) | [Pre-registration](https://doi.org/10.17605/OSF.IO/MA6YD) | [Replication Repository](https://github.com/hayden-farquhar/Traveller-Fever-Differential)

## What it does

BEACON produces a ranked differential diagnosis for a febrile patient who has recently returned from overseas travel. Given the travel destination, symptoms, exposures, incubation period, and vaccination status, it outputs:

- **Top-10 ranked diagnoses** with posterior probabilities
- **Per-factor evidence breakdown** showing how the prior, symptoms, exposures, and incubation each contribute
- **Must-not-miss safety alerts** for malaria, measles, VHF, and mpox — with cited clinical guidelines
- **Explicit abstention** when the model cannot discriminate

## Quick start

```bash
pip install -e .
streamlit run app/streamlit_app.py
```

## How it works

BEACON is a Naive Bayes classifier with:
- **33 diagnoses** across tropical, vaccine-preventable, and non-tropical diseases
- **Australian-weighted priors** from GeoSentinel reweighted by NNDSS imported-case distributions
- **Graded symptom likelihood ratios** (11 features) calibrated against Bottieau 2007 (N=2,071)
- **Monthly-updated outbreak signals** from WHO Disease Outbreak News
- **Peaked triangular incubation distributions** using published typical periods

## NOT a substitute for clinical judgement

This tool is designed to support — not replace — clinical decision-making. Always:
- Request malaria thick/thin film and RDT for any febrile traveller from an endemic area
- Consider isolation precautions for measles, mpox, and VHF
- Use clinical context, examination findings, and laboratory results alongside this tool

## Citation

Farquhar H. BEACON: An Australian-weighted Bayesian diagnostic differential for febrile returned travellers with live outbreak priors. 2026. Pre-registered at https://doi.org/10.17605/OSF.IO/MA6YD

## Licence

Code: MIT. Clinical knowledge data: CC-BY-4.0.
