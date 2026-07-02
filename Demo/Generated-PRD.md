# Project Health Dashboard - PRD

**Version:** 1.0
**Date:** February 13, 2026

### OBJECTIVE
Provide leadership with real-time, at-a-glance visibility into the health and potential overruns of active projects to enable proactive intervention and informed decision-making.

### PROBLEM STATEMENT
Leadership currently operates with a significant blind spot regarding the ongoing health and financial status of active projects, relying solely on lagging quarterly reports. This lack of immediate insight prevents timely identification of projects at risk of overrunning their budgets, leading to reactive management and potential financial losses. Project Managers also spend valuable time manually compiling project health reports for various stakeholders.

### SOLUTION
The Project Health Dashboard will be a web-based, desktop-optimized application providing a consolidated view of all active projects. It will feature a Traffic Light System (RAG: Red, Amber, Green) to indicate project status, with 'Red' signifying projects exceeding their monthly budget burn by more than 10%. The dashboard will source data from the existing ERP system, utilizing a middle-layer Redis cache to overcome data latency and API rate limits, ensuring a near real-time status view. A key feature for Project Managers will be the ability to export the dashboard view as a PDF for easy stakeholder reporting.

### TRADEOFFS

*   **Exact Dollar Amount vs. Percentage Variance for Overrun:**
    *   **Decision:** Initial implementation will show percentage variance (>10% over monthly burn for 'Red' status).
    *   **Pros :** Simplifies the visual representation, provides a quick understanding of severity relative to budget, potentially less sensitive data for initial rollout.
    *   **Cons :** Lacks the absolute financial impact clarity on overall portfolio. May not be sufficient for detailed financial analysis by leadership.

*   **Direct ERP API Call vs. Middle-Layer Cache (Redis):**
    *   **Decision:** Implement a middle-layer Redis cache.
    *   **Pros:** Addresses the ERP system's daily sync latency, providing a more "current" status. Mitigates ERP API rate limits, preventing service disruptions if multiple users refresh simultaneously. Improves dashboard load times for users.
    *   **Cons:** Adds technical complexity and infrastructure overhead. Introduces a slight delay between the ERP update and the cache update (though still much faster than daily sync). Requires maintenance of an additional data layer.

*   **Mobile-First Design vs. Desktop-Only for MVP:**
    *   **Decision:** Desktop-only for MVP.
    *   **Pros :** Significantly reduces initial development time and effort, allowing for faster time-to-market for the core functionality. Focuses resources on the primary use case (leadership/PMs at their desks).
    *   **Cons:** Limits accessibility for users who primarily work from mobile devices, potentially requiring them to wait for a future iteration to access the dashboard conveniently on the go.


###  DOGS NOT BARKING (Unaddressed Considerations)

* **User Roles & Permissions:** The current design implies leadership sees all projects and PMs see their portfolio, but explicit roles (e.g., viewing, admin) and corresponding access controls for sensitive project data were not discussed.
* **Data Refresh Frequency (User Perspective):** While a Redis cache is planned, the user-facing refresh interval (e.g., "Data updated X minutes ago") and whether PMs can trigger an on-demand refresh for their specific projects were not defined.
* **Drill-Down Capabilities:** The dashboard is described as a "glance" view. No discussion occurred regarding the ability for users to click on a project to view more detailed information, trends, or specific budget lines.
* **Filtering and Search:** With potentially many active projects, how users will navigate or find specific projects (e.g., by department, PM, project type) was not addressed.
* **Historical Data/Trends:** The dashboard provides a snapshot of current health. The ability to view project health trends over time, which could be crucial for deeper analysis, was not discussed.
* **Definition of "Monthly Burn":** While mentioned as a metric, the exact calculation and source of "monthly burn" (e.g., actual spend vs. planned spend for the month) were not explicitly detailed.

### CONSTRAINTS
*   **Data Latency:** The primary ERP system only syncs once a day, meaning truly "live" project status is not directly achievable without a caching layer.
*   **ERP API Rate Limits:** Direct, frequent calls to the ERP API will result in blocking, necessitating an intermediary solution.
*   **MVP Scope:**
    *   Desktop-only view (no mobile responsiveness for MVP).
    *   Project status indicated via a Traffic Light System (RAG).
    *   Over-budget status (Red) defined as >10% over monthly burn (percentage variance, not exact dollar amount).
    *   Mandatory PDF export feature.
*   **Technical Implementation:**
    *   Use of Redis for the middle-layer cache.
    *   Use of 'ReportLab' Python library for PDF generation.



---------------------------------------------------------------------

# APPENDIX
### Meeting Notes

**Transcript: Project Health Dashboard - Initial Kickoff**
*   **Date:** Feb 10, 2026
*   **Attendees:** Sarah (PM), David (Design)
*   **Key Discussion Points:**
    *   Leadership lacks visibility into project overruns, only seeing quarterly reports.
    *   Need a 'Project Health' dashboard for at-a-glance status.
    *   Dashboard to use a grid view with a Traffic Light (RAG) system: Green (on track), Amber (at risk), Red (over budget).
    *   Red status defined as >10% over monthly burn (percentage variance, not exact dollar amount for now).
    *   PMs need to view their full portfolio.
    *   PDF export is a must-have for MVP to assist PMs with stakeholder reporting.

**Transcript: Project Health Dashboard - Tech Review**
*   **Date:** Feb 12, 2026
*   **Attendees:** Sarah (PM), Mike (Eng)
*   **Key Discussion Points:**
    *   Dashboard concept (Traffic Light, PDF export) is clear.
    *   **Technical Challenge 1 (Data Latency):** ERP system syncs only once a day; 'current' status requires addressing this.
    *   **Technical Challenge 2 (API Rate Limits):** Direct ERP API hits would cause blocking if many users refresh.
    *   **Solution for Data/API Issues:** Implement a middle-layer cache (e.g., Redis) to store the latest pull.
    *   **PDF Export Implementation:** Use 'ReportLab' library in Python backend.
    *   **MVP Scope Clarification:** Mobile First view is deferred; focus on Desktop-only for MVP to save time.

### Action Items

| Action Item                                | Owner | Completion Date |
| :----------------------------------------- | :---- | :-------------- |
| Develop initial UI/UX mockups for Desktop-only dashboard with RAG system and project grid. | David | Feb 20, 2026    |
| Research and design Redis caching strategy for ERP data integration. | Mike  | Feb 23, 2026    |
| Investigate 'ReportLab' library integration for PDF export functionality. | Mike  | Feb 23, 2026    |
| Draft detailed functional specifications for PM portfolio view and RAG calculation logic. | Sarah | Feb 21, 2026    |
| Schedule follow-up meeting with Mike (Eng) and David (Design) to review mockups and tech plan. | Sarah | Feb 24, 2026    |