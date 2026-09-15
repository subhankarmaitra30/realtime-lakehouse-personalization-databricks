## Phase 0 — Engineering Foundation

Completed the professional repository setup and Databricks workspace integration.

### Key Components Implemented

* GitHub repository with production-style folder structure
* Local development environment configured with Git Bash and VS Code
* Databricks Repos integration with GitHub for version-controlled notebooks
* Databricks cluster configured using ML runtime
* Initial Lakehouse database (`ecommerce_lakehouse`) created

### Purpose

This phase establishes the foundational infrastructure required to implement the Databricks Lakehouse architecture.
It ensures reproducibility, proper project organization, and seamless synchronization between local development, GitHub, and Databricks.

### Status

✅ Phase 0 Completed
Next Phase → **Phase 1: Real-Time Event Simulation and Data Generation**

```
====================================================================================================
               TRI-TIER COLLABORATIVE GOVERNANCE & EXECUTION TOPOLOGY
====================================================================================================

               TIER 1: FOUNDER & VENTURE LEADERSHIP (Deep Neuro-Nex Pvt. Ltd.)
                    • Managing Director & Principal Architect: Subhankar Maitra
                    • Strategic Direction, System Invariants, IP Prosecution (Patent 202631094668)
                    • Defense Liaison (iDEX, Army Design Bureau, DG AFMS) & Clinical MoUs
                                                │
                                                ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ TIER 2: INTERNAL VENTURE CORE ENGINEERING TEAM (Dedicated Company Employees / Equity-Vested)     │
│                                                                                                  │
│   [LEAD HARDWARE & EMBEDDED SYSTEMS ENGINEER]       [LEAD SYSTEMS SOFTWARE & DL COMPILER ENG]    │
│   • Owns synthesizable RTL, bare-metal Rust drivers • Owns CUDA C++ kernels, TensorRT execution  │
│   • Manages PCB bring-up, PCIe Gen 6 DMA memory      • Manages 6-DoF SLAM & CvRDT mesh stacks    │
│   • Direct gatekeeper inside IIT Madras labs         • Maintains private production git repos    │
└───────────────────────────────────────────────┬──────────────────────────────────────────────────┘
                                                │ Joint SRA Work Package Execution & Co-Dev Sprints
                                                ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ TIER 3: IIT MADRAS SRA INSTITUTIONAL LABS & RESEARCH PERSONNEL (Sponsored via SRA Allocation)    │
│                                                                                                  │
│  [ELECTRICAL & HIGH-SPEED HARDWARE]      [CRYPTOGRAPHY & DISTRIBUTED SYSTEMS]                    │
│  • Dept. of Electrical Engineering /     • Secure Systems Centre / Trusted Computing Lab         │
│    High-Speed Digital & RF Lab           • Hardware TEE Enclaves (AMD SEV-SNP / TrustZone)       │
│  • High-Voltage Medical Safety Chamber   • Plonky2 ZK-SNARKs & Bare-Metal CvRDT Verification     │
│                                                                                                  │
│  [COMPUTATIONAL BIOPHYSICS & AI]         [CLINICAL ANALYTICS & INTERVENTIONAL SLAM]              │
│  • Centre for Programmable Photonic &    • Healthcare Technology Innovation Centre (HTIC)        │
│    Neuromorphic Systems / HPC Centre     • Calibrated Hydrophone Tanks & Optical Motion Analysis │
│  • TensorRT Compilation & SE(3) Mamba    • Sub-16ms Direct Video Compositor & 3D Voxel Meshing   │
│                                                                                                  │
│  [DEFENSE RUGGEDIZATION & MECHATRONICS]  [CLINICAL SITE INTEGRATION (PGIMER / AIIMS)]            │
│  • Centre for Robotics & Mechatronics    • Clinical Research & Data Liaison Fellows              │
│  • IITM Telecom & Defense Testing Centre • 20,000+ Patient Trajectory Validation Pipeline        │
│  • MIL-STD-810H / 461G / 1275E Hardening • Ground-Truth Matching (Radiology to LIS Pathology)    │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```
```
               SPRINT-BY-SPRINT DUAL-TRACK COLLABORATIVE WORKFLOW
               
 [ FOUNDER / ARCHITECT ] ────> Defines Non-Negotiable Invariants & Milestone Gates
                                           │
                                           ▼
 [ INTERNAL CORE TEAM ]  ────> Writes Synthesizable RTL, Bare-Metal Firmware, CUDA Drivers
 (HW & SW Leads)                           │
                                           ▼ [Hands Off Tested Assemblies for Formal Validation]
 [ SRA LABS & FELLOWS ]  ────> Executes Chamber Testing, Hydrophone Runs, Clinical Integration
 (IITM / HTIC PIs)                         │
                                           ▼
 [ FORMAL STAMPED AUDIT] ────> Produces Certified Test Dossier for iDEX Milestone Clearance
```

```
                GRANT CAPITAL ALLOCATION ARCHITECTURE (₹1.50 Cr BASELINE)
┌──────────────────────────────────────────────────────────────────────────┬──────────┬─────────────┐
│ Expenditure Classification & Operational Budget Head                     │ Ratio    │ Allocation  │
├──────────────────────────────────────────────────────────────────────────┼──────────┼─────────────┤
│ 1. Capital Expenditure (CapEx - High-Speed Hardware, Silicon, Kits)      │ 25.0%    │ ₹37.50 L    │
│ 2. Internal Core Engineering Team Payroll (Company-Vested Engineers)     │ 25.0%    │ ₹37.50 L    │
│ 3. IIT Madras Institutional SRA Contract (HTIC & Partner Labs)           │ 25.0%    │ ₹37.50 L    │
│ 4. Defense Test Chambers & Environmental Certification (NABL/MIL-STD)    │ 10.0%    │ ₹15.00 L    │
│ 5. Clinical Trial Logistics & Hospital Data Tap Operations (PGIMER)      │  7.5%    │ ₹11.25 L    │
│ 6. Statutory IP Prosecution (Complete Patent Spec, PCT) & Regulatory DHF │  7.5%    │ ₹11.25 L    │
└──────────────────────────────────────────────────────────────────────────┴──────────┴─────────────┘
```
```
                               BUDGET ALLOCATION PIE GRAPH
                  ┌────────────────────────────────────────────────────────┐
                  │ [■■■■■■■■■■■■]    CapEx: Hardware, Silicon & BOM (25%) │
                  │ [■■■■■■■■■■■■]    Internal Core Team Payroll (25%)     │
                  │ [■■■■■■■■■■■■]    IIT Madras SRA Contract (25%)        │
                  │ [■■■■■]           Defense Chambers & NABL Cert (10%)   │
                  │ [■■■■]            Clinical Operations & PGIMER (7.5%)  │
                  │ [■■■■]            IP Prosecution & Regulatory (7.5%)   │
                  └────────────────────────────────────────────────────────┘
```





























