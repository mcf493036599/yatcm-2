# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_rdkit.models.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cas', models.CharField(blank=True, max_length=1024, null=True, verbose_name='CAS Registry Number')),
                ('url', models.URLField(blank=True, max_length=1024, verbose_name='URL link to chemfinder database.')),
            ],
            options={
                'verbose_name_plural': 'CAS',
            },
        ),
        migrations.CreateModel(
            name='ChEMBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chembl_id', models.BigIntegerField(blank=True, null=True, verbose_name='ChEMBL ID')),
                ('url', models.URLField(blank=True, max_length=1024, verbose_name='URL link to ChEMBL database.')),
            ],
            options={
                'verbose_name_plural': 'ChEMBL ID',
            },
        ),
        migrations.CreateModel(
            name='CID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.BigIntegerField(blank=True, null=True, verbose_name='PubChem Compound Identification')),
                ('url', models.URLField(blank=True, max_length=1024, verbose_name='URL link to PubChem.')),
            ],
            options={
                'verbose_name_plural': 'CID',
            },
        ),
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_created=True)),
                ('english_name', models.CharField(blank=True, max_length=1024)),
                ('chinese_name', models.CharField(blank=True, max_length=1024)),
                ('phonetic_name', models.CharField(blank=True, max_length=1024)),
                ('synonyms', models.CharField(blank=True, max_length=1024)),
                ('first_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024)),
                ('chinese_name', models.CharField(blank=True, max_length=1024)),
                ('phonetic_name', models.CharField(blank=True, max_length=1024)),
                ('medicinal_part', models.CharField(blank=True, max_length=1024)),
                ('img', models.ImageField(blank=True, null=True, upload_to='herb_images/')),
                ('image_url', models.URLField(blank=True, max_length=1024)),
                ('wiki_link', models.URLField(blank=True)),
                ('wiki_chinese', models.URLField(blank=True)),
                ('compounds', models.ManyToManyField(blank=True, to='compounds.Compound')),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smiles', models.CharField(blank=True, max_length=1024)),
                ('mol', django_rdkit.models.fields.MolField(blank=True, null=True)),
                ('mol_block', models.TextField(blank=True)),
                ('bfp', django_rdkit.models.fields.BfpField(blank=True, null=True)),
                ('mol_file', models.FileField(blank=True, null=True, upload_to='mol_files/')),
                ('mol_image', models.ImageField(blank=True, null=True, upload_to='mol_images/')),
                ('formula', models.CharField(blank=True, max_length=1024)),
                ('mol_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('alogp', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Calculated ALogP')),
                ('hba', models.SmallIntegerField(blank=True, null=True, verbose_name='Number hydrogen bond acceptors')),
                ('hbd', models.SmallIntegerField(blank=True, null=True, verbose_name='Number hydrogen bond donors')),
                ('psa', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Polar surface area')),
                ('rtb', models.SmallIntegerField(blank=True, null=True, verbose_name='Number rotatable bonds')),
                ('first_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='TCMTaxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024)),
                ('unique_name', models.CharField(blank=True, max_length=1024)),
                ('chinese_name', models.CharField(blank=True, max_length=1024)),
                ('phonetic_name', models.CharField(blank=True, max_length=1024)),
                ('taxonomy_id', models.BigIntegerField(blank=True, null=True)),
                ('name_class', models.CharField(blank=True, max_length=1024)),
                ('ncbi_link', models.URLField(blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='compounds.TCMTaxonomy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='herb',
            name='taxonomy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compounds.TCMTaxonomy'),
        ),
        migrations.AddField(
            model_name='compound',
            name='structure',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='compounds.Structure'),
        ),
    ]
