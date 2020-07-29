#!/usr/bin/env bash

[ -z "$1" ] && exit 1

python2 \
  obj-debug-dmd-no-sccache/dist/bin/dmd.py \
  --sort-by slop \
  --max-frames 6 \
  --allocation-filter "Channel::Channel" \
  "$1" > `basename "$1" .json.gz`

# char input_cmsg_buf_[Channel::kReadBufferSize + kControlBufferSlopBytes];
# size = 4128
#
# 4 blocks in heap block record 1 of 2,433
# 49,152 bytes (34,688 requested / 14,464 slop)
# Individual block sizes: 12,288 x 4
# 0.43% of the heap (0.43% cumulative)
# 34.95% of unreported (34.95% cumulative)
#
#
# char input_cmsg_buf_[(size_t)((Channel::kReadBufferSize + kControlBufferSlopBytes) / 4)];
# size = 1032
#
# 4 blocks in heap block record 1 of 2,458
# 32,768 bytes (22,304 requested / 10,464 slop)
# Individual block sizes: 8,192 x 4
# 0.29% of the heap (0.29% cumulative)
# 34.48% of unreported (34.48% cumulative)
#
#
# char input_cmsg_buf_[(size_t)((Channel::kReadBufferSize + kControlBufferSlopBytes) / 8)];
# size = 516
#
# 4 blocks in heap block record 1 of 2,357
# 32,768 bytes (20,256 requested / 12,512 slop)
# Individual block sizes: 8,192 x 4
# 0.29% of the heap (0.29% cumulative)
# 34.40% of unreported (34.40% cumulative)# 34.29% of unreported (34.29% cumulative)
#
#
# char input_cmsg_buf_[(size_t)((Channel::kReadBufferSize + kControlBufferSlopBytes) / 16)];
# size = 258
#
# 4 blocks in heap block record 1 of 2,379
# 32,768 bytes (19,232 requested / 13,536 slop)
# Individual block sizes: 8,192 x 4
# 0.29% of the heap (0.29% cumulative)
# 34.14% of unreported (34.14% cumulative)
#
#
# char input_cmsg_buf_[(size_t)((Channel::kReadBufferSize + kControlBufferSlopBytes) / 32)];
# size = 129
#
# 4 blocks in heap block record 1 of 2,367
# 32,768 bytes (18,720 requested / 14,048 slop)
# Individual block sizes: 8,192 x 4
# 0.29% of the heap (0.29% cumulative)
# 34.21% of unreported (34.21% cumulative)
