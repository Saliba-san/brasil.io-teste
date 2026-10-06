#!/usr/bin/env bash
# Executado pelo runner após readiness; preparação pertence à aplicação.
set -euo pipefail
: "${SECURITY_COMPOSE_PROJECT:?Projeto de integração obrigatório}"
: "${SECURITY_COMPOSE_FILE:?Snapshot Compose obrigatório}"

docker compose --project-name "$SECURITY_COMPOSE_PROJECT" \
  --file "$SECURITY_COMPOSE_FILE" exec -T web \
  python manage.py prepara_integracao
