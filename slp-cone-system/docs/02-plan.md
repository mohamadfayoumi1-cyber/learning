# 02 — Team Split, Timeline and Risks

Roles and schedule are expressed in terms of the feature IDs from
[`00-functional-spec.md`](00-functional-spec.md), so progress is measured against the
specification rather than against effort spent.

## 1. Team split

Four students, four vertical slices. Each owns a slice end to end — design, build, test,
and the corresponding report chapter — so that nobody's mark depends on somebody else's
subsystem working.

| Role | Student | Owns | Features |
|---|---|---|---|
| **Mechanical** | MECH | Chassis, drivetrain geometry, wheel and motor selection, cone shell and impact strategy, CG and tip-over analysis, weatherproofing, CAD and manufacture, battery access | NFR-11, NFR-12, NFR-15, F5.4 (mechanical side) |
| **Embedded & Power** | MECA-1 | Electronics integration, wiring or PCB, power system and BMS, motor drivers, firmware base, encoder and IMU drivers, wheel PID, self-test, safety interlocks in firmware | F6.2, F6.3, F6.5, F6.6, F6.7, F5.2, F5.4, F5.5, F5.7, F5.8, NFR-8 |
| **Localisation & Comms** | MECA-2 | Anchor infrastructure and survey, UWB ranging, EKF pose fusion, ESP-NOW protocol and gateway, calibration routines, the ground-truth camera rig | F6.1, F7.1, F7.3, F5.3, NFR-1, NFR-2, NFR-6 |
| **Coordination & UI** | MECA-3 | Coordinator service, simulator, layout compiler, assignment, ORCA planner, tablet application, logging | F1.\*, F2.\*, F3.\*, F4.\*, F8.\*, F5.1, F5.6, NFR-3, NFR-13, NFR-14 |

**Shared, and scheduled explicitly rather than assumed:** system integration, the test
campaign in §7.3 of the specification, the report, the presentation and the video.

**The two interfaces that must be frozen early**, because they are where the four slices
meet and where integration projects usually fail:

1. The **cone command and telemetry message set** — between MECA-1 and MECA-2/3.
2. The **coordinator ↔ cone abstraction** — so MECA-3 can develop against the simulator
   while the hardware is still on the bench.

Freeze both by the end of Week 6 and treat changes to them as change requests, not edits.

## 2. Timeline

Two semesters, roughly fifteen weeks each. Milestones are stated as demonstrable
outcomes, not as activities.

### Semester 1 — Fall 2026: prove the concept

| Weeks | Milestone | Done when |
|---|---|---|
| 1–2 | Specification frozen | §9 questions answered by the advisor; fleet size, pad and heading requirement fixed |
| 3–4 | Architecture and interfaces frozen | Message set and coordinator↔cone abstraction documented and agreed by all four |
| 3–6 | **Simulator running** | 6 simulated cones move from a drawn path to targets with assignment and ORCA, with injected noise and packet loss. MECA-3 is now unblocked permanently |
| 4–8 | Cone unit v1 | One chassis drives under manual command; encoders and PID closed; CAD released for the shell |
| 6–10 | Localisation bench | UWB ranging to 4 anchors, raw accuracy characterised, EKF fusing odometry and IMU |
| 9–12 | **One cone drives to a commanded point autonomously** | Position error measured against the camera rig. This is the semester's critical result |
| 12–14 | Tablet application v1 | Draw, validate, preview and execute against the simulator |
| 15 | **Semester 1 review** | Live demo: one real cone driving to tablet-specified points; simulator showing 6 |

The Week 9–12 milestone is the project's go/no-go point. If a single cone cannot reach a
commanded position within tolerance, the swarm work has nothing to stand on — escalate
immediately rather than proceeding to build more units.

### Semester 2 — Spring 2027: make it a system

| Weeks | Milestone | Done when |
|---|---|---|
| 1–3 | Fleet of 4 built | Four units assembled from the v1 design with shells fitted |
| 2–5 | **Two cones avoid each other** | Head-on and crossing conflicts resolved, on hardware. The first genuine swarm result |
| 4–7 | Full fleet coordination | Four cones deploy a preset layout; NFR-3 and NFR-7 measured |
| 6–9 | Safety features complete | F5.1–F5.8 implemented and provoked; NFR-9 measured |
| 8–11 | Robustness | Tip detection and re-deploy (F3.8), battery management (F6.7), knock-over recovery |
| 10–12 | **Test campaign** | The §7.3 verification matrix executed and the evidence collected |
| 12–14 | Deliverables | Report, presentation, subtitled video, source code, schematics, CAD |
| 15 | **Defence** | The four-minute demonstration sequence, rehearsed |

## 3. Sequencing rules

Three rules that matter more than the dates:

1. **Simulator before hardware.** Three of the four slices can progress without a physical
   cone. Any week in which MECA-3 is blocked on the machine shop is a planning failure.
2. **One, then two, then four.** Two cones is where collision avoidance becomes real, and
   it is a much harder step than two-to-four. Do not build four units before two work.
3. **Build the measurement rig before you need the measurements.** The overhead-camera
   ground truth and the F8.2 accuracy log should exist by Week 8 of Semester 1. Every
   test run afterwards then generates report evidence for free.

## 4. Risk register

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Outdoor UWB accuracy worse than 25 cm | High — NFR-1 fails | Medium | Characterise by Week 10 of Semester 1. Raise anchors on poles, improve anchor geometry, fuse harder. Fall back to indoor demonstration with a camera, which §9 flags as a decision to take early rather than late |
| Wheel slip and traction on asphalt | Medium — accuracy and ETA suffer | Medium | Wheels ≥ 100 mm with rubber tread, torque margin ≥ 3×, closed-loop control, and UWB correcting odometry drift continuously |
| Budget cannot cover six units | Medium — reduced demonstration | Medium | Design for six, build two, prove, then replicate. The specification's minimum demonstrable product needs only four |
| Integration compressed into the final weeks | High — classic capstone failure | High | The frozen interfaces in §1 and the simulator exist specifically to make integration continuous instead of terminal |
| Mechanical durability under vehicle contact | Medium | Medium | Resolve §9 question 5 early. Compliant sacrificial shell, isolated electronics, low CG |
| One student's slice slips and blocks the others | High | Medium | Vertical slices plus the simulator mean each slice degrades independently rather than blocking the rest |
| Scope creep from the swarm literature | Medium | High | §8 of the specification is the defence. Anything outside the Must set waits |

## 5. What to do first

In order, starting now:

1. Take §9 of the functional specification to the advisor and close all five questions.
2. Freeze the fleet size and the pad assumption; update §3 of the specification.
3. Agree the two interfaces in §1 and write them down.
4. Start the simulator. It is the longest pole that has no dependencies.
