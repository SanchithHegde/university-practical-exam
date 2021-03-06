# Generated by Django 3.1.3 on 2020-11-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('region', models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeHasDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.college')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('semester', models.PositiveSmallIntegerField()),
                ('course_type', models.CharField(choices=[('Core', 'Core'), ('Elective', 'Elective')], default='Core', max_length=8, verbose_name='Type')),
                ('num_credits', models.PositiveSmallIntegerField(verbose_name='Number of credits')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField()),
                ('slot', models.PositiveSmallIntegerField()),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('college_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.collegehasdepartment', verbose_name='College and Department')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('years_experience', models.PositiveSmallIntegerField(verbose_name='years of experience')),
                ('college_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.collegehasdepartment', verbose_name='College and Department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('admission_year', models.PositiveSmallIntegerField(verbose_name='year of admission')),
                ('semester', models.PositiveSmallIntegerField()),
                ('college_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.collegehasdepartment', verbose_name='College and Department')),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_id', models.CharField(max_length=10, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField()),
                ('college_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.collegehasdepartment', verbose_name='College and Department')),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.department'),
        ),
        migrations.AddField(
            model_name='collegehasdepartment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.department'),
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_dept_day_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_scheduling.timetable', verbose_name='College and Department')),
                ('end_usn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='end_usn', to='exam_scheduling.student')),
                ('ext_examiner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ext_examiner', to='exam_scheduling.teacher', verbose_name='External Examiner')),
                ('int_examiner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='int_examiner', to='exam_scheduling.teacher', verbose_name='Internal Examiner')),
                ('lab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam_scheduling.lab')),
                ('start_usn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='start_usn', to='exam_scheduling.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='timetable',
            constraint=models.UniqueConstraint(fields=('college_dept', 'day', 'slot'), name='college_dept_day_slot'),
        ),
        migrations.AddConstraint(
            model_name='timetable',
            constraint=models.UniqueConstraint(fields=('college_dept', 'date', 'start_time', 'end_time'), name='college_dept_date_time'),
        ),
        migrations.AddConstraint(
            model_name='timetable',
            constraint=models.UniqueConstraint(fields=('college_dept', 'course'), name='college_dept_course'),
        ),
        migrations.AddConstraint(
            model_name='lab',
            constraint=models.UniqueConstraint(fields=('id', 'college_dept'), name='college_lab'),
        ),
        migrations.AddConstraint(
            model_name='courseoffering',
            constraint=models.UniqueConstraint(fields=('course', 'teacher'), name='course_teacher'),
        ),
        migrations.AddConstraint(
            model_name='collegehasdepartment',
            constraint=models.UniqueConstraint(fields=('college', 'department'), name='college_dept'),
        ),
        migrations.AddConstraint(
            model_name='allocation',
            constraint=models.UniqueConstraint(fields=('college_dept_day_slot', 'lab'), name='college_dept_day_slot_allocation'),
        ),
        migrations.AddConstraint(
            model_name='allocation',
            constraint=models.UniqueConstraint(fields=('college_dept_day_slot', 'int_examiner'), name='college_dept_day_slot_int_examiner'),
        ),
        migrations.AddConstraint(
            model_name='allocation',
            constraint=models.UniqueConstraint(fields=('college_dept_day_slot', 'ext_examiner'), name='college_dept_day_slot_ext_examiner'),
        ),
    ]
