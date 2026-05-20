#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#  @Time   :2025/2/28 13:18
#  @Author :Zhd
#  @File   :app.py.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 任务列表
tasks = []

class Task:
    def __init__(self, description, priority='normal'):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} [{self.priority}] - {status}"

# 首页路由
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)
    # return "hello app.py!"
# 添加任务路由
@app.route('/add', methods=['POST'])
def add_task():
    description = request.form.get('description')
    priority = request.form.get('priority', 'normal')
    task = Task(description, priority)
    tasks.append(task)
    return redirect(url_for('index'))

# 标记任务完成路由
@app.route('/complete/<int:task_index>')
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index].mark_completed()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)