# Generated by Django 2.1 on 2018-10-13 15:24

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main_website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('maillist', models.BooleanField(default=True)),
                ('telephone_num', models.CharField(max_length=15, verbose_name='Telephone Number')),
                ('address', models.TextField(max_length=30)),
                ('suburb', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=4)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=30)),
                ('balance', models.FloatField(default=0)),
                ('has_identified', models.BooleanField(default=False)),
                ('state', models.CharField(choices=[('NSW', 'New South Wales'), ('QLD', 'Queensland'), ('SA', 'South Australia'), ('TAS', 'Tasmania'), ('VIC', 'Victoria'), ('WA', 'Western Australia')], default='QLD', max_length=3)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', main_website.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('product_status', models.CharField(choices=[('ONLOAN', 'ON LOAN'), ('RETURNTODAY', 'RETURN TODAY'), ('RETURNLATE', 'RETURN LATE'), ('RESERVED', 'RESERVED'), ('COLLECTTODAY', 'COLLECT TODAY'), ('COLLECTLATE', 'COLLECT LATE')], default='RESERVED', max_length=12)),
            ],
            options={
                'verbose_name': 'Loan',
            },
        ),
        migrations.CreateModel(
            name='LendingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('product_status', models.CharField(choices=[('ONLOAN', 'ON LOAN'), ('RETURNTODAY', 'RETURN TODAY'), ('RETURNLATE', 'RETURN LATE'), ('RESERVED', 'RESERVED'), ('COLLECTTODAY', 'COLLECT TODAY'), ('COLLECTLATE', 'COLLECT LATE')], max_length=12)),
            ],
            options={
                'verbose_name': 'Loan history',
                'verbose_name_plural': 'Loan histories',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('maintenance_id', models.AutoField(primary_key=True, serialize=False)),
                ('maintenance_status', models.CharField(choices=[('0', 'Ok'), ('1', 'At Repairer'), ('2', 'With Staff Member')], max_length=1)),
                ('maintenance_location', models.CharField(max_length=255)),
                ('maintenance_notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpeningDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('opening_hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_payment_id', models.CharField(blank=True, max_length=27, null=True)),
                ('stripe_payment_date', models.DateTimeField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('long_description', models.TextField()),
                ('short_description', models.CharField(max_length=50)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('available_on', models.DateField(blank=True, null=True)),
                ('shown', models.BooleanField(default=True)),
                ('added_on', models.DateField(auto_now_add=True, null=True)),
                ('code', models.CharField(max_length=8)),
                ('brand', models.CharField(max_length=32)),
                ('price_paid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('loan_period', models.IntegerField(default=7)),
                ('components', models.TextField()),
                ('care_information', models.TextField()),
                ('keywords', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('alt', models.CharField(blank=True, max_length=128)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main_website.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='users')),
                ('verified', models.BooleanField(default=False)),
                ('alt', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='IdentificationImage',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='identification', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.FileField(upload_to=main_website.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='membership', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('membership_type', models.CharField(choices=[('g', 'Guest'), ('m', 'Member')], default='g', max_length=1)),
                ('start_time', models.DateField(blank=True, null=True)),
                ('end_time', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userimage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_website.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_website.ProductCondition'),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_website.ProductLocation'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_website.ProductTag'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordernote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lendinghistory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='history_product', to='main_website.Product'),
        ),
        migrations.AddField(
            model_name='lendinghistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lending',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='main_website.Product'),
        ),
        migrations.AddField(
            model_name='lending',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_website.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]