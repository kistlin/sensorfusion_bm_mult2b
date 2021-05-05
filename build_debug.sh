#!/bin/sh
cmake -DCMAKE_TOOLCHAIN_FILE="armgcc.cmake" -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=debug  .
make -j 2>&1 | tee build_log.txt
