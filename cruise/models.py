from django.db import models


class ChiefScientist(models.Model):
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    first_name = models.CharField(primary_key=True, max_length=50, verbose_name="First Name")  # The composite primary key (first_name, last_name) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'CHIEF_SCIENTIST'
        unique_together = (('first_name', 'last_name'),)


class DataType(models.Model):
    data_type = models.CharField(primary_key=True, max_length=10, verbose_name="Data Type",
                                 help_text='Acronymn assigned to this specific Data Type')
    long_description = models.CharField(max_length=75, blank=True, null=True, verbose_name="Description",
                                        help_text='Long Description for this specific Data Type Acronym')

    class Meta:
        managed = False
        db_table = 'DATA_TYPE'


class DeliveryStage(models.Model):
    stage = models.CharField(primary_key=True, max_length=1, verbose_name="Delivery Stage")

    class Meta:
        managed = False
        db_table = 'Delivery_Stage'


class ProcessState(models.Model):
    state = models.CharField(primary_key=True, max_length=1, verbose_name="Process State")

    class Meta:
        managed = False
        db_table = 'Process_State'


class Cruise(models.Model):
    cruise_number = models.CharField(primary_key=True, max_length=20, verbose_name="Cruise Number",
                                     help_text='Cruise number assigned eg: HUD2011009')  # The composite primary key (cruise_number, leg) found, that is not supported. The first column is selected.
    meds_cruise_number = models.CharField(max_length=20, blank=True, null=True,verbose_name="MEDS Cruise Number",
                                          help_text='MEDS Mission number assigned eg:18HUD11009')
    platform = models.CharField(max_length=50, blank=True, null=True, verbose_name="Platform",
                                help_text='Ship name or other platform name Eg: HUDSON')
    leg = models.CharField(max_length=10, verbose_name="Leg",
                           help_text='1-2 digit Leg number.  0 if single Leg.  UK if non-standard Cruise of unknown legs.')
    year = models.CharField(max_length=20, verbose_name="Year",
                            blank=True, null=True, help_text='4 digit year')
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date",
                                  help_text='Official Start of the Cruise Eg: day sailed or switched Legs')
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date",
                                help_text='Official Start of the Cruise Eg: day switched Legs or returned to port')
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Location",
                                help_text='General names of All locations surveyed on Cruise Eg: Scotian Shelf, Labrador Sea, Georges Bank')

    last_name = models.CharField(max_length=200,blank=True, null=True, help_text='Last Name of Chief Scientist')
    first_name = models.CharField(max_length=50, blank=True, null=True, help_text='First Name of Chief Scientist')

    organizations = models.CharField(max_length=255, blank=True, null=True, verbose_name="Organizations",
                                     help_text='Acronyms of all Organizations participating in Cruise')
    cruisereport_received = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cruise Report Received",
                                             help_text='Y or N Received from Chief Scientist')
    creport_sent = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cruise Report Sent",
                                    help_text='ARCHIVE and/or LIBRARY (was BIO and SABS) - Locations where Cruise Report can be found')
    ship_code = models.CharField(max_length=4, blank=True, null=True, verbose_name="Ship Code",
                                 help_text='FK TO VESSEL TABLE')
    bridgelog_archived = models.CharField(max_length=20, blank=True, null=True, verbose_name="Bridgelog Archived",
                                          help_text='Y or N Archived Scanned Bridge Log scanned or H Hydro Log spreadsheet archived or L Log Lost')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name="Comments")

    class Meta:
        managed = False
        db_table = 'Cruise'
        unique_together = (('cruise_number', 'leg'),)
