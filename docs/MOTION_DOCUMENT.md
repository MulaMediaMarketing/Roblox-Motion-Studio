# Motion Document

The motion document is the canonical interchange format.

Conceptual shape:

```text
MotionDocument
  metadata
  skeleton
  duration
  sampleRate
  tracks
    joint
      translation keys
      rotation keys
      scale keys
  events
  markers
```

Rotations are represented as quaternions in the domain model.

The document is editable and deterministic. Renderers and exporters must not mutate it implicitly.
