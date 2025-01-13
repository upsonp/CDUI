from django.db import models


class ChiefScientist(models.Model):
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    first_name = models.CharField(primary_key=True, max_length=50,
                                  verbose_name="First Name")  # The composite primary key (first_name, last_name) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'CHIEF_SCIENTIST'
        unique_together = (('first_name', 'last_name'),)


class DataType(models.Model):
    data_type = models.CharField(primary_key=True, max_length=10, verbose_name="Data Type",
                                 help_text='Acronymn assigned to this specific Data Type')
    long_description = models.CharField(max_length=75, blank=True, null=True, verbose_name="Description",
                                        help_text='Long Description for this specific Data Type Acronym')

    def __str__(self):
        return self.data_type

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

    meds_cruise_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="MEDS Cruise Number",
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

    last_name = models.CharField(max_length=200, blank=True, null=True, help_text='Last Name of Chief Scientist')
    first_name = models.CharField(max_length=50, blank=True, null=True, help_text='First Name of Chief Scientist')

    organizations = models.CharField(max_length=255, blank=True, null=True, verbose_name="Organizations",
                                     help_text='Acronyms of all Organizations participating in Cruise')
    cruisereport_received = models.CharField(max_length=255, blank=True, null=True,
                                             verbose_name="Cruise Report Received",
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


class Data(models.Model):
    id = models.BigIntegerField(primary_key=True, help_text='new field?',
                                verbose_name="ID")  # The composite primary key (id, project_number) found, that is not supported. The first column is selected.

    year = models.CharField(max_length=4, blank=True, null=True, help_text='Year the information was entered EG: 2012',
                            verbose_name="Year")
    project_number = models.CharField(max_length=3,
                                      help_text='Assigned consecutively as projects come in each year eg: 01',
                                      verbose_name="Project Number")

    # this is a composite key into the Cruise Table
    leg = models.CharField(max_length=10, blank=True, null=True,
                           help_text='1-2 digit Leg number.  0 if single Leg.  UK if non-standard Cruise of unknown legs.',
                           verbose_name="Leg")
    cruise_number = models.CharField(max_length=20, blank=True, null=True,
                                     help_text='Cruise number associated with the data eg: HUD2011009',
                                     verbose_name="Cruise Number")

    # It takes forever to get the DataType from the DataType table with this model setup where a DataType is a string
    # data_type = models.ForeignKey('DataType', models.DO_NOTHING, db_column='data_type', blank=True, null=True,
    #                               help_text='Each data type on a cruise will have its own entry eg: MCTD',
    #                               verbose_name="Data Type")

    # It's way faster to get the DataType as a string as it appears in the Data table
    data_type = models.CharField(max_length=10, blank=True, null=True,
                                 help_text='Each data type on a cruise will have its own entry eg: MCTD',
                                 verbose_name="Data Type")

    date_entered = models.CharField(max_length=10, blank=True, null=True,
                                    help_text='Date the entry was put into the  table eg:11/01/2012',
                                    verbose_name="Date Entered")
    status = models.CharField(max_length=13, blank=True, null=True, help_text='PROCESSED, NOT PROCESSED or INACTIVE',
                              verbose_name="Status")
    first_name = models.CharField(max_length=50, blank=True, null=True,
                                  help_text='First Name of Data Owner / PI Principal Investigator',
                                  verbose_name="First Name")
    last_name = models.CharField(max_length=200, blank=True, null=True,
                                 help_text='Last Name of Data Owner / PI Principal Investigator',
                                 verbose_name="Last Name")
    datatech = models.CharField(max_length=16, blank=True, null=True,
                                help_text='Name of the person processing the data', verbose_name="Data Tech")
    date_completed = models.CharField(max_length=10, blank=True, null=True,
                                      help_text='Date the complete data set was processed',
                                      verbose_name="Date Completed")
    agency = models.CharField(max_length=19, blank=True, null=True,
                              help_text='Division or Company to whom the data belongs', verbose_name="Agency")
    project_name = models.CharField(max_length=50, blank=True, null=True,
                                    help_text='Name of the project, usually found on the log sheet',
                                    verbose_name="Project Name")
    number_of_inst = models.CharField(max_length=10, blank=True, null=True,
                                      help_text='Number of Stations or instruments containing data',
                                      verbose_name="No. of Instruments")
    comments = models.CharField(max_length=199, blank=True, null=True,
                                help_text='Any Comments, including data location', verbose_name="Comments")
    delivery_stage = models.ForeignKey('DeliveryStage', models.DO_NOTHING, db_column='delivery_stage', blank=True,
                                       null=True, help_text='new field?', verbose_name="Delivery Stage")
    process_state = models.ForeignKey('ProcessState', models.DO_NOTHING, db_column='process_state', blank=True,
                                      null=True, help_text='new field?', verbose_name="Process State")

    class Meta:
        managed = False
        db_table = 'data'
        unique_together = (('id', 'project_number'),)
        ordering = ['id', 'project_number']
