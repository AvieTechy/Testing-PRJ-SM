# Environmental Needs

## Base System Hardware
| Component        | Specification                                                 | Notes                                      |
|------------------|---------------------------------------------------------------|--------------------------------------------|
| Server (local)   | CPU: 4 cores, RAM: 8 GB, Storage: 50 GB                       | Runs backend application and database      |
| Client machines  | CPU: Dual-core 2 GHz, RAM: 4 GB, Disk: 10 GB                  | Student laptops used for front-end testing |
| Network          | Stable Wi-Fi 50 Mbps+                                        | Required to ensure performance tests with JMeter |

## Base Software Elements in the Test Environment
| Software Element | Version / Toolchain                           | Purpose                                 |
|------------------|------------------------------------------------|-----------------------------------------|
| OS (client)      | Windows 10/11, Ubuntu 20.04                   | Operating systems for testers’ machines |
| Browsers         | Chrome 126, Firefox 128, Edge 126             | Official cross-browser testing targets  |
| Backend          | Laravel 8.x, PHP 8.x                          | Web application backend framework       |
| Database         | MySQL 8.x                                     | Stores product, order, and user data    |
| Containerization | Docker 24.x                                   | Rapid setup for backend and database    |

## Productivity and Support Tools
| Tool             | Usage                                                        |
|------------------|--------------------------------------------------------------|
| Postman/Newman   | API testing and automated collection execution in CI/CD      |
| Selenium WebDriver | GUI/UI automation testing                                  |
| JMeter           | Performance testing (load, stress, spike)                    |
| GitHub Issues    | Bug tracking, change requests, and defect management         |
| Google Sheets    | Test Case management, Incident Logs, Traceability Matrix     |
| GitHub Actions   | CI/CD pipeline for automated test suites                     |

## Test Environment Configurations
| Configuration Type  | Details                                                                |
|---------------------|------------------------------------------------------------------------|
| Localhost setup     | Backend and database deployed via Docker Compose on student machines   |
| Browser configs     | Chrome (Windows/Linux), Firefox (Ubuntu), Edge (Windows)               |
| Minimal config      | Client laptop with 2 GB RAM running Chrome to validate basic usability |
| Average config      | Client laptop with 4 GB RAM, stable Chrome/Firefox for main testing    |
| Performance config  | JMeter run on 8 GB RAM machine simulating 50–200 virtual users         |
| Accessibility check | Basic screen reader test (NVDA on Windows) – optional                  |

\newpage