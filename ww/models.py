from django.db import models
# Create your models here.


class abort_record(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vin = models.CharField(max_length=32)
    vvid = models.CharField(max_length=32)
    reason_code = models.CharField(max_length=8)
    account = models.CharField(max_length=32)
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'abort_record'


class abort_classification(models.Model):
    id = models.BigIntegerField(primary_key=True)
    reason = models.CharField(max_length=256)
    code = models.CharField(max_length=8)
    belong = models.CharField(max_length=256)

    class Meta:
        db_table = 'abort_classification'


class qc_tl_interval(models.Model):
    id = models.BigIntegerField(primary_key=True)
    qcid = models.CharField(max_length=128)
    vvid = models.CharField(max_length=128)
    start = models.DateTimeField()
    end = models.DateTimeField()
    interval = models.IntegerField()
    type = models.CharField(max_length=256)
    classification = models.CharField(max_length=256)
    reason = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    origin = models.CharField(max_length=10)
    deleted = models.IntegerField()
    create_on = models.DateTimeField()
    update_on = models.DateTimeField()

    class Meta:
        db_table = '`wfm_job`.`qc_tl_interval`'


class jobs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vehicle_id = models.CharField(max_length=256)
    job_id = models.CharField(max_length=256)
    job_status = models.IntegerField()
    job_content = models.CharField(max_length=10000)
    create_on = models.DateTimeField()
    update_on = models.DateTimeField()

    class Meta:
        db_table = '`wfm_job`.`jobs`'
