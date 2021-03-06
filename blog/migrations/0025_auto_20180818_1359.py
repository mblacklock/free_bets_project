# Generated by Django 2.0.7 on 2018-08-18 12:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmath.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20180817_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('equation', wagtailmath.blocks.MathBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('resize_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('xl', 'XL')]))]))], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('equation', wagtailmath.blocks.MathBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('resize_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('xl', 'XL')]))]))], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('equation', wagtailmath.blocks.MathBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('resizable_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('xl', 'XL')]))]))], blank=True, null=True),
        ),
    ]
