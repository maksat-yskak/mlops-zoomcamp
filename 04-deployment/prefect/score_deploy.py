from prefect.deployments import Deployment
from prefect.client.schemas.schedules import CronSchedule
from score import ride_duration_prediction

deployment = Deployment.build_from_flow(
    flow=ride_duration_prediction,
    name="ride_duration_prediction",
    parameters={
        "taxi_type": "green",
        "run_id": "820d3f851eb6426d9c1dfb2e1bf4d9a9",
    },
    schedules=[CronSchedule(cron="0 3 2 * *")],
    work_queue_name="ml",
)

deployment.apply()