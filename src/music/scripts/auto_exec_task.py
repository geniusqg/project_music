# coding:utf-8

import include
import django
django.setup()
from erp_api.models import EvalTask
from erp_api.judge_process import EvalTaskProcess
import time


def auto_compute_price():
    '''search record from EvalTask then compute the price'''
    while True:
        eval_task_list = EvalTask.objects.all().order_by('-task_create_time')
        for eval_task in eval_task_list:
            if eval_task.applystate not in ['4','5','6']:
                auto_process = EvalTaskProcess(eval_task.id)
                auto_process.auto_compute_process()
        time.sleep(60)


def execute():
    auto_compute_price()

if __name__ == '__main__':

    execute()