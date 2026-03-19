# Activity Sequencing Logic

## Dependency Network (RC Water Tank)
```
Mobilization
 -> Site Clearing (FS)
   -> Excavation (FS)
     -> Formation Compaction (FS)
       -> Blinding (FS)
         -> WP Membrane (FS, parallel with rebar start)
         -> Base Slab Rebar (FS, lag 5d after blinding)
           -> Base Slab Concrete (FS)
             -> Kicker (FS)
               -> Wall Rebar L1 (FS)
                 -> Wall Formwork L1 (SS, lag 3d)
                   -> Wall Concrete L1 (FS)
                     -> Wall Rebar L2 (FS, after cure)
                       -> Wall Concrete L2 (FS)
                         -> Columns (FS)
                           -> Roof Beam Formwork (FS)
                             -> Roof Beam Rebar (SS, lag 2d)
                               -> Roof Slab Formwork (FS)
                                 -> Roof Slab Rebar (SS, lag 3d)
                                   -> Roof Concrete (FS)
                                     -> Formwork Strike (FS, lag 7d)
                                       -> Internal WP (FS)
                                         -> External WP (SS, parallel)
                                           -> Backfill (FS)
                                             -> M&E (SS, can start earlier)
                                               -> Tank Filling (FS)
                                                 -> Hydrostatic Test (FS, 7d/cell)
                                                   -> Leak Repair (FS)
                                                     -> Commissioning (FS)
                                                       -> Handover (FS)
```

## Dependency Types
- FS: Finish-to-Start (most common)
- SS: Start-to-Start (with lag, for overlapping activities)
- Lag: minimum delay between linked activities

## Critical Path
Mobilization -> Excavation -> Blinding -> Base Rebar -> Base Concrete -> Walls -> Columns -> Roof -> Testing -> Handover

## Float Activities
- WP membrane under slab (overlaps with early rebar)
- External WP (parallel with internal)
- M&E (starts during roof construction)
- Backfill (lags behind WP by weeks)
