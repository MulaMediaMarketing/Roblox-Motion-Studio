# Kinetic Studio Architecture

## Product boundary

Kinetic Studio is an animation authoring application, not an AI-chat application.

Primary workflows:
1. Hand-key animation.
2. Video-to-motion without prompts.
3. Optional AI-assisted editing.
4. Export to target runtimes.

## Layered architecture

```
Presentation
  React + TypeScript + Three.js
        |
Application
  editor state / commands / timeline / selection
        |
Domain
  skeleton / pose / keyframes / curves / blending / events
        |
Adapters
  R15 / future Unreal and other skeletons
        |
Infrastructure
  video decoding / pose inference / storage / export
```

The domain layer must not depend on React, Three.js, FastAPI, MediaPipe, or Roblox.

## Core rule

Use a neutral animation document as the contract between systems:

Video -> Motion Extraction -> Animation Document -> Editor -> Target Exporter

This prevents the application from becoming a Roblox-specific collection of scripts.

## Module sizing

- Prefer focused modules.
- Target under 1,000 lines per source file.
- 1,200 lines is the absolute ceiling without an explicit architecture decision.
- No god classes, god services, or hidden cross-module state.
- A small number of cohesive modules is preferred over hundreds of trivial files.

## Rendering

Three.js is the presentation/runtime viewport. It consumes the domain skeleton and pose state through a renderer adapter.

## Timeline

The timeline is Maya-inspired in capability, not in visual complexity:
- Dope-sheet style keyframes.
- Expandable joint tracks.
- Selection, snapping, copy/paste.
- Continuous interpolation.
- Smooth pose blending.
- Event tracks.
- Non-destructive editing.
- Graph editor can be added later.

## Video motion

Prompts are optional. The primary video workflow is:

Video -> pose estimation -> 3D motion -> retarget -> cleanup -> editable keyframes.

## Export

Exporters consume the neutral animation document. Roblox R15 is the first exporter. Future exporters can target other skeletons without rewriting the editor.
