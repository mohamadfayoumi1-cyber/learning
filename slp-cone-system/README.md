# Collaborative Training Cone System

Senior Learning Project (SLP), 2026–2027 · Advisor: Ahmad Koubeissi · 1 MECH + 3 MECA

A swarm of self-driving traffic cones for driver training. An instructor draws or selects
an exercise on a tablet; the cones assign themselves to positions and drive there together
without colliding. Selecting a different exercise rearranges the pad in under a minute.

## Documents

| Doc | What it answers |
|---|---|
| **[`docs/00-functional-spec.md`](docs/00-functional-spec.md)** | **What the system does.** Feature catalogue (F1–F8), use cases, tablet screens, non-functional requirements, MoSCoW prioritisation, verification matrix, scope boundaries. **Start here.** |
| [`docs/01-architecture.md`](docs/01-architecture.md) | *How* it does it. The four defining design decisions, subsystem specs, control cascade, stack recommendation |
| [`docs/02-plan.md`](docs/02-plan.md) | Who builds what, when. Team split, two-semester milestones, risk register |

The functional specification is authoritative. If the architecture conflicts with it, the
architecture changes.

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
