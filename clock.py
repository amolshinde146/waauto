
from apscheduler.schedulers.blocking import BlockingScheduler
from sms import Wa_sms


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(Wa_sms, 'interval', seconds=10)
