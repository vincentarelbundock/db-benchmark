#!/usr/bin/env python

print("# join-pydatatable.py", flush=True)

import os
import gc
import timeit
import datatable as dt
from datatable import f, sum, join

exec(open("./helpers.py").read())

ver = dt.__version__
git = dt.__git_revision__
task = "join"
solution = "pydatatable"
fun = "join"
cache = "TRUE"

data_name = os.environ['SRC_JN_LOCAL']
src_jn_x = os.path.join("data", data_name+".csv")
y_data_name = join_to_tbls(data_name)
src_jn_y = [os.path.join("data", y_data_name[0]+".csv"), os.path.join("data", y_data_name[1]+".csv"), os.path.join("data", y_data_name[2]+".csv")]
if len(src_jn_y) != 3:
    raise Exception("Something went wrong in preparing files used for join")

print("loading datasets " + data_name + ", " + y_data_name[0] + ", " + y_data_name[2] + ", " + y_data_name[2], flush=True)

x = dt.fread(src_jn_x)
small = dt.fread(src_jn_y[0])
medium = dt.fread(src_jn_y[1])
big = dt.fread(src_jn_y[2])

print(x.nrows, flush=True)
print(small.nrows, flush=True)
print(medium.nrows, flush=True)
print(big.nrows, flush=True)

y = small.copy()
t_start = timeit.default_timer()
y.key = 'id1'
ans = x[:, :, join(y)] # , on='id1'
y = medium.copy()
y.key = 'id2'
ans = x[:, :, join(y)] # , on='id2'

print("joining...", flush=True)

question = "small inner on int" # q1
gc.collect()
y = small.copy() # https://github.com/h2oai/datatable/issues/1080
t_start = timeit.default_timer()
y.key = 'id1'
ans = x[:, :, join(y)] # , on='id1'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
y = small.copy()
t_start = timeit.default_timer()
y.key = 'id1'
ans = x[:, :, join(y)] # , on='id1'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

question = "medium inner on int" # q2
gc.collect()
y = medium.copy()
t_start = timeit.default_timer()
y.key = 'id2'
ans = x[:, :, join(y)] # , on='id2'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
y = medium.copy()
t_start = timeit.default_timer()
y.key = 'id2'
ans = x[:, :, join(y)] # , on='id2'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

#question = "medium outer on int" # q3
#gc.collect()
#y = medium.copy()
#t_start = timeit.default_timer()
#y.key = 'id2'
#ans = x[:, :, join(y, how='left')] # , on='id2'
#print(ans.shape, flush=True)
#t = timeit.default_timer() - t_start
#m = memory_usage()
#t_start = timeit.default_timer()
#chk = ans[:, [sum(f.v1), sum(f.v2)]]
#chkt = timeit.default_timer() - t_start
#write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
#del ans
#gc.collect()
#y = medium.copy()
#t_start = timeit.default_timer()
#y.key = 'id2'
#ans = x[:, :, join(y, how='left')] # , on='id2'
#print(ans.shape, flush=True)
#t = timeit.default_timer() - t_start
#m = memory_usage()
#t_start = timeit.default_timer()
#chk = ans[:, [sum(f.v1), sum(f.v2)]]
#chkt = timeit.default_timer() - t_start
#write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
#print(ans.head(3).to_pandas(), flush=True)
#print(ans.tail(3).to_pandas(), flush=True)
#del ans

question = "medium inner on factor" # q4
gc.collect()
y = medium.copy()
t_start = timeit.default_timer()
y.key = 'id5'
ans = x[:, :, join(y)] # , on='id5'
t_start = timeit.default_timer()
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
y = medium.copy()
t_start = timeit.default_timer()
y.key = 'id5'
ans = x[:, :, join(y)] # , on='id5'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

question = "big inner on int" # q5
gc.collect()
y = big.copy()
t_start = timeit.default_timer()
y.key = 'id3'
ans = x[:, :, join(y)] # , on='id3'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans
gc.collect()
y = big.copy()
t_start = timeit.default_timer()
y.key = 'id3'
ans = x[:, :, join(y)] # , on='id3'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans

exit(0)
