# coding=utf8

u'''
添加方法前，请先看一下这个说明：
    现在这种方式有个小问题，如果你的方法回和 MYSQL 有交互
    请务必在查询前调用下django.db 的 close_old_connections 方法
'''

# django apps
import include
import django.db
# 初始化djagno环境
django.setup()
from erp_api.models import EvalTask
from erp_api.judge_process import EvalTaskProcess
import datetime
# our apps
from tools import main,fixed_time_task,fixed_interval_task


def hour_interval():
    print 'start'
    print 'run hour interval task when ', datetime.datetime.now()

# ============  work  =================

# 1次/分钟，计算评估价格
def auto_compute_price():
    '''search record from EvalTask then compute the price'''
    django.db.close_old_connections()
    eval_task_list = EvalTask.objects.all().order_by('-task_create_time')
    for eval_task in eval_task_list:
        if eval_task.applystate in ['0','1','2','3']:
            print 'eval task %s auto evaluation start'%eval_task.id
            auto_process = EvalTaskProcess(eval_task.id)
            auto_process.auto_compute_process()
            #print 'task state is %s'%eval_task.applystate
            print 'eval task %s auto evaluation finished'%eval_task.id

fixed_interval_task(hour_interval, seconds=3600)
fixed_time_task(auto_compute_price, hour=3, minute=0)


# 每天00:00，抓取erp数据
from evaluation.views import scheduled_process as get_data_ERP
fixed_time_task(get_data_ERP, hour=0, minute=0)


if __name__ == '__main__':
    main()

