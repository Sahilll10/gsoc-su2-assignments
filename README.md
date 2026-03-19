# SU2 GSoC 2026 Assignments

**Contributor:** Sahil Kumar  
**GitHub:** [Sahilll10](https://github.com/Sahilll10)  
**Project Interest:** Project AMR — Quick Adaptive Mesh Refinement for 2D Test Cases

## Contents

### Assignment 1: Compile SU2
SU2 v8.4.0 compiled from source on Ubuntu 24.04 with GCC 13.3.0 using Meson 1.10.1. Both serial and MPI builds completed successfully. All standard tutorials ran without errors.

### Assignment 2: Axisymmetric Turbulent Jet
2D axisymmetric turbulent jet simulated using INC_RANS with SST k-omega. Mesh generated with gmsh. See `assignment2/report.md`.

### Assignment 3: Python Wrapper — Unsteady CHT Flat Plate
Unsteady CHT flat plate run using `pysu2.CSinglezoneDriver` with time-varying wall temperature. See `assignment3/report.md`.

### Assignment 4: Spatially Varying Wall Temperature
Flat plate with sinusoidal wall temperature T(x) = 300 + 50*sin(2*pi*x/0.5) K applied per vertex via Python wrapper. See `assignment4/report.md`.

### Assignment 5: Speed of Sound — New Volume and Screen Output
Added local speed of sound as a new output field in `CFlowCompOutput.cpp`. Confirmed value of 347.22 m/s consistent with freestream at T=300 K. See `assignment5/report.md`.

## SU2 Pull Requests
- [PR #2750](https://github.com/su2code/SU2/pull/2750) — Fix C++17 Boost unary_function build failure in tecio (merged)
- [PR #2755](https://github.com/su2code/SU2/pull/2755) — Fix unsteady testcase configs and add regression tests (under review)
