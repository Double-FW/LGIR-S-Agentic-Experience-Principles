# Weekly Hugging Face publication

Destination: https://huggingface.co/datasets/GarethFW/LGIR-S_Agentic_Experience_Principles

1. In [Actions variables](https://github.com/Double-FW/LGIR-S-Agentic-Experience-Principles/settings/variables/actions), add or edit `HF_DATASET_ID` to `GarethFW/LGIR-S_Agentic_Experience_Principles`. This is an ordinary variable.
2. At https://huggingface.co/settings/tokens create a fine-grained token. Select only `GarethFW/LGIR-S_Agentic_Experience_Principles` and grant repository read/write access. Do not grant broad user, inference or billing permissions. Never paste the token into a document or chat.
3. In [Actions secrets](https://github.com/Double-FW/LGIR-S-Agentic-Experience-Principles/settings/secrets/actions), create `HF_TOKEN` and paste the token into its Secret field.
4. Open [the workflow](https://github.com/Double-FW/LGIR-S-Agentic-Experience-Principles/actions/workflows/huggingface-sync.yml), choose Run workflow, select main and run. Check its result and the destination Files tab.

The workflow is configured for Mondays at 09:41 UTC (09:41 UK winter; 10:41 UK summer). GitHub can delay scheduled runs and disable schedules in inactive public repositories. A successful installation does not establish that publication has run; verify the manual run first.

The existing destination must already exist. Only the 14 named managed files are updated, in one guarded commit. Unrelated files, including `.gitattributes`, are preserved. The source must remain public. Publication stops on source, licence, target or validation errors. The token is supplied only to the publishing step. The automation exports committed source material; it does not adopt requirements or verify product performance. No-change runs do not create destination commits.

For local verification, install `huggingface/requirements.txt`, then run `python scripts/check_repository.py` and `python -m unittest discover -s tests -v`. Export with `python scripts/export_huggingface.py --output /tmp/lgirs-preview --dataset-id GarethFW/LGIR-S_Agentic_Experience_Principles`. Publication additionally requires HF_TOKEN and a real existing dataset; tests use a simulated destination.
