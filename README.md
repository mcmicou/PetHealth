# 🐾 PetHealth.AI

An AI-powered SaaS that analyzes pet health data from vet records, smart collars, and photos to give personalized insights.

---

## 🧩 Tech Stack
- **Frontend:** Next.js (TypeScript + React)
- **Backend:** FastAPI (Python)
- **Database:** Postgres (via Docker)
- **Cache / Queue:** Redis (via Docker)

---

## 🧠 Getting Started

### 1️⃣ Backend Setup
```bash
cd apps/api
source .venv/bin/activate
python -m uvicorn app.main:app --reload --port 8000