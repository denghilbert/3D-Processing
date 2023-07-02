#!/bin/bash

# colmaping
ns-process-data images --data ~/Desktop/eu_colmap/colmap/images --output-dir ~/Desktop/eu_colmap/

# generate mask
ns-process-data images --data ~/Desktop/eu_colmap/colmap/images --output-dir ~/Desktop/eu_colmap/ --skip-colmap
