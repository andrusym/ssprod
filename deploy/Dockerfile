
# Use multi-stage build for frontend and backend
FROM node:18 as frontend-builder
WORKDIR /app/frontend
COPY skystrike-prod-release-9.3.13/frontend ./ 
RUN npm install && npm run build

FROM python:3.10-slim as backend
WORKDIR /app
COPY skystrike-prod-release-9.3.13/backend ./backend
COPY skystrike-prod-release-9.3.13/.env .env
COPY --from=frontend-builder /app/frontend/dist ./frontend_dist
RUN pip install --no-cache-dir -r backend/requirements.txt

EXPOSE 8501
CMD ["python", "backend/main.py"]
