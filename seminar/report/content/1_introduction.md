# Introduction

## Group Information

The team consists of 5 members with clearly defined roles to ensure schedule adherence and research quality:

| Role | Member | Primary Responsibilities |
|------|--------|--------------------------|
| Team Lead | Cao Nhi | Coordination, AI research in Performance Testing, consolidation & presentation |
| Member | Thanh Thuý | Foundational research & business flow analysis |
| Member | Minh Trí | Tool comparison, scenario design & JMeter scripting |
| Member | Cát Tường | In-depth JMeter study (architecture, components) & test plan design |
| Member | Việt Tú | Environment setup, test execution, demo preparation |

\pagebreak

## Overview

### Motivation

Performance is a critical factor shaping the user experience of any web application. A system may provide a rich interface and complete functionality, but if it responds slowly or fails under heavy traffic, users will quickly abandon it. In practice, poor performance has often led to revenue loss, reputational damage, and difficulty in scaling operations.

For this reason, Performance Testing is considered an essential step in the software development lifecycle. At the same time, the recent progress in Artificial Intelligence (AI) opens up new opportunities: faster analysis of large volumes of test data, automated anomaly detection, and improved accuracy in diagnosing performance issues. These aspects motivated us to pursue the topic “Performance Testing with Apache JMeter and AI-assisted Analysis.”

### Research Problem

The study focuses on addressing three key questions:

- How can we select the most suitable testing tool among the many available solutions?
- What is the proper way to design scenarios that closely reflect real user behavior?
- At which stages of the Performance Testing cycle can AI provide meaningful support?

### Objectives

1. Standardize the concepts and scope of Performance Testing, with emphasis on Load, Stress, Spike, and Endurance tests.
2. Compare major performance testing tools (JMeter, NeoLoad, WebLOAD, LoadUI, LoadRunner) in terms of strengths, limitations, and usage contexts.
3. Gain practical knowledge of Apache JMeter, including its architecture, components, and scripting process.
4. Explore the potential of AI techniques (e.g., anomaly detection, log/result analysis).
5. Build and execute a complete testing scenario on JPetStore (Register → Login → Purchase → Payment).
6. Collect results, perform analysis, and deliver findings in the form of a written report, presentation, and demonstration.

### Scope

1. **In scope**

- Theoretical study of Performance Testing types (Load, Stress, Spike, Endurance).
- Tool comparison at an overview level with key technical criteria.
- Experiments on a demo environment (not production).
- Proof-of-concept (POC) exploration of AI in result analysis.

2. **Out of scope**

- Advanced topics such as Security, Penetration, or Mobile Performance Testing.
- Development of new testing tools from scratch.
- Optimization of real production infrastructure.

### Project Roadmap

| Phase                             | Weeks | Main Activities                                       | Status    |
| --------------------------------- | ----- | ----------------------------------------------------- | --------- |
| Phase 1: Foundation & Research    | 1–3   | Theoretical study, tool comparison, JMeter setup      | Completed |
| Phase 2: Design & Execution       | 4–7   | Scenario design, scripting, test execution, AI trials | Upcoming  |
| Phase 3: Reporting & Presentation | 8–9   | Final report, slides, demo video                      | Pending   |

### Stakeholders

| Type      | Stakeholder           | Expectations                                      |
| --------- | --------------------- | ------------------------------------------------- |
| Academic  | Supervisor            | Quality of research and practical contribution    |
| Students  | Class peers           | Reference for methodology and results             |
| Community | Testers / Researchers | Insights on AI application in Performance Testing |

### Risks and Mitigation

| Risk                                           | Impact                   | Mitigation                                               |
| ---------------------------------------------- | ------------------------ | -------------------------------------------------------- |
| Insufficient machine resources under high load | Distorted measurements   | Use profiling, separate load generator and target system |
| Scripts not reflecting realistic user behavior | Low validity of results  | Validate scenarios with business logic early             |
| Poor AI model performance                      | False anomalies          | Supplement with statistical baselines, tune parameters   |
| Delay in Phase 2 execution                     | Time pressure in Phase 3 | Finalize scenarios early, assign tasks in parallel       |

### Document Structure

1. **Chapter 1 – Introduction**: Context, objectives, scope, methodology.
2. **Chapter 2 – Theoretical Foundations**: Performance Testing concepts, AI support areas, tool comparison.
3. **Chapter 3 – Apache JMeter**: Overview, installation, architecture & components, basic exercises.
4. **Chapter 4 – Experimental Demonstration (JPetStore)**: Scenarios, test data & parameters, execution results, AI-assisted analysis.

\newpage
