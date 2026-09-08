# Collaborative Training Cone System

Senior Learning Project (SLP), 2026–2027 · Advisor: Ahmad Koubeissi · 1 MECH + 3 MECA

A swarm of self-driving traffic cones for driver training. An instructor draws or selects
an exercise on a tablet; the cones assign themselves to positions and drive there together
without colliding. Selecting a different exercise rearranges the pad in under a minute.

## The document

**[`SLP_Cone_System_Design_Specification.pdf`](SLP_Cone_System_Design_Specification.pdf)** —
22 pages, everything in one typeset document. This is the deliverable: hand it to the
advisor.

| | Contents |
|---|---|
| Front | Cover, document control, identifier conventions, contents |
| **Part I** | **Functional Specification** — §1–10. What the system does, and the basis on which it will be assessed |
| **Part II** | **System Architecture** — §11–14. One defensible way of meeting Part I, with each choice argued against what was rejected |
| **Part III** | **Execution** — §15–19. Team split, two-semester schedule, sequencing rules, risk register |
| Appendices | A: all 53 features with priority and owner · B: every derived number with its source section · C: glossary |

Six figures: the feature map, the tablet Map screen, system topology, software
decomposition, the cone state machine, and the two-semester schedule.

**Part I is authoritative.** If the architecture conflicts with it, the architecture
changes.

### Sources

The PDF is generated from HTML in [`pdf/`](pdf/) — see [`pdf/README.md`](pdf/README.md) to
rebuild. The three files in [`docs/`](docs/) are the working drafts the document was built
from; they are convenient to read and diff on GitHub, but the PDF is the fuller and
authoritative version.

## Feature areas at a glance

| | Area | Headline capability |
|---|---|---|
| **F1** | Course authoring | Draw or dimension an exercise; validated against the live fleet as you draw |
| **F2** | Layout library | Seven standard driving exercises built in; save your own; chain them into a lesson |
| **F3** | Deployment | Preview the assignment, execute, and get an unambiguous READY before the vehicle moves |
| **F4** | Monitoring | Live map, per-cone battery and link health, alerts, session log |
| **F5** | Safety | E-stop, comms watchdog, geofence, tip detection, vehicle-present interlock |
| **F6** | Cone autonomy | Self-localise, drive to pose, hold position, avoid neighbours, self-test |
| **F7** | Administration | Pad survey, fleet registration, calibration, diagnostics |
| **F8** | Data | Accuracy and session records, exportable — and the evidence base for the report |

## The demonstration to build toward

Four cones. Load the slalom preset, change the spacing, preview, execute — the cones cross
the area simultaneously and settle. READY appears. Load a parking bay and execute again.
Knock a cone over; the system detects it, alerts, and re-deploys it once righted. Press
E-STOP mid-motion; everything halts.

Four minutes, and it exercises every *Must* feature in the specification.

## Two decisions that need the advisor

Both are in [§9 of the functional spec](docs/00-functional-spec.md#9-open-questions-for-the-advisor)
and both change the design significantly:

1. **Indoors or outdoors?** Indoors, an overhead camera gives ~1 cm accuracy for the cost
   of one camera. Outdoors that fails and the project needs UWB, which is the single
   highest-risk subsystem.
2. **Is heading control required?** Cones are rotationally symmetric. If heading does not
   matter, a substantial slice of the localisation work disappears.

## Status

Design phase — specification and architecture only. No code yet; see `docs/02-plan.md`.
