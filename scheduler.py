    """
    This schedules and actually operates the reminder schedules
    """
    from apscheduler.schedulers.background import BackgroundScheduler
    from plyer import notification 

    #Need to set up call back
    def run_reminders(reminder):
        notification.notify(
            title = "NOVA Reminder",
            message=reminder.message,
            timeout = 10
        )
    #Setting up the sched function
    def schedule_reminders(loaded_reminders):
        scheduler = BackgroundScheduler()
        for rem in loaded_reminders:
            if rem.enabled:
                scheduler.add_job(
                func= run_reminders,
                trigger=rem.trigger,
                args = [rem],
                id = rem.id
                )
        scheduler.start()
        try:
            while True:
                sleep()
        except KeyboardInterrupt:
            scheduler.shutdown()
