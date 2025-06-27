    """
    This schedules and actually operates the reminder schedules
    """
    from loader import load_reminders
    from apscheduler.schedulers.background import BackgroundScheduler
    