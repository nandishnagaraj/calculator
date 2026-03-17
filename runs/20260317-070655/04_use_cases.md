```markdown
## Use Case: Employee Requests Leave

**Goal:** An employee successfully requests time off, and their manager approves or rejects it.

**Actors:**
*   **Primary Actor:** Employee (Emily Chen)
*   **Secondary Actors:** Manager (Mark Johnson), HR Administrator (Sarah Miller - for initial setup)

**Preconditions:**
*   Employee has an active ZenLeave account and is logged in. (REQ-001)
*   Employee has available leave balance for the requested leave type. (REQ-004)
*   Leave types and company holidays are configured by an HR Admin. (REQ-013, REQ-015)
*   Employee has a designated manager in the system. (REQ-012)

**Main Flow:**

1.  **Employee logs in** to ZenLeave. (REQ-001)
2.  **Employee navigates to the "Request Leave" section.**
3.  **Employee selects a leave type, start date, end date, and provides an optional reason.** (REQ-005)
    *   System calculates the duration.
4.  **Employee submits the leave request.** (REQ-005)
5.  **System validates the request** (e.g., sufficient balance, no overlaps, not on a company holiday). (REQ-005)
6.  **System records the request as "Pending".** (REQ-006)
7.  **System sends an automated notification to the Employee's Manager.** (REQ-005, REQ-018)
8.  **Manager logs in** and views pending requests on their dashboard. (REQ-009, REQ-019)
9.  **Manager reviews the request details** and employee's history/balance. (REQ-009, REQ-011)
10. **Manager approves the leave request.** (REQ-009)
11. **System updates the request status to "Approved".** (REQ-006)
12. **System adjusts the Employee's leave balance** for the approved leave type. (REQ-004)
13. **System sends an automated notification to the Employee** about the approval. (REQ-018)
14. **System updates the Manager's Team Leave Calendar** to reflect the approved leave. (REQ-010)

**Alternate Flows:**

*   **A1: Insufficient Leave Balance (from Step 5):**
    *   System displays an error: "Insufficient balance for selected leave type."
    *   Employee can modify dates/type or cancel. (REQ-005)
*   **A2: Overlapping Leave Request (from Step 5):**
    *   System displays an error: "You already have a pending or approved request for these dates."
    *   Employee can modify dates or cancel. (REQ-005)
*   **A3: Employee Cancels Pending Request (from Step 6/7):**
    *   Employee views pending requests and selects "Cancel Request". (REQ-007)
    *   System changes status to "Cancelled" and notifies Manager. (REQ-007, REQ-018)
*   **A4: Manager Rejects Leave Request (from Step 10):**
    *   Manager selects "Reject" and adds optional comments. (REQ-009)
    *   System updates status to "Rejected" and notifies Employee. (REQ-006, REQ-018)
    *   Employee's leave balance remains unchanged.

**Postconditions:**
*   Employee's leave request is in a final state (Approved, Rejected, or Cancelled).
*   Employee's leave balance is updated if the request was approved. (REQ-004)
*   Manager's team calendar reflects the updated leave status. (REQ-010)
*   All actions are recorded in the system's audit log. (REQ-017)
*   Relevant actors receive automated notifications. (REQ-018)
```

# Actors
(TODO: generated content missing — please fill)


# Preconditions
(TODO: generated content missing — please fill)


# Main Flow
(TODO: generated content missing — please fill)


# Alternate Flows
(TODO: generated content missing — please fill)


# Postconditions
(TODO: generated content missing — please fill)
