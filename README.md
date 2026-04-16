**Serverless Retail Intelligence Orchestrator**

**Highlights**

- Event-driven Lambda architecture.
- Workflow orchestration via Step Functions.
- Automated ETL + enrichment pipeline.
- Secure RBAC authorization.
- External supplier API integration.

**Advanced System Design**

        ┌──────────────┐
        │ API Gateway  │
        └──────┬───────┘
               │
        Order Ingestion Lambda
               │
        Step Function Workflow
               │
     ┌─────────┼─────────┐
     │                   │
Inventory Sync     Data Enrichment

     │                   │
 External APIs        Processed Data
 
     │                   │
     
     └──────────► Storage Layer
