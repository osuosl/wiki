.. _s3-storage:

Using S3 Object Storage
=======================

.. contents::

The OSL provides S3-compatible object storage backed by our Ceph cluster. Once
we have created a bucket for your project and delivered your access keys, you
can use any S3-compatible client to upload, download, and manage your data.

What you need
-------------

- Your **access key** and **secret key**. We deliver these through the Secrets
  app on our Nextcloud instance at `cloud.osuosl.org <https://cloud.osuosl.org>`_
  -- never by email or chat. If you have not received them yet, or have lost
  them, contact us at support@osuosl.org.
- The name of your bucket. Bucket names follow the scheme
  ``<project>-<bucket>`` (for example, ``fooproject-backups``).
- An S3-compatible client such as ``s3cmd``, the AWS CLI, ``rclone``, or a
  library like ``boto3``.

Endpoint
--------

All clients connect to our RADOS Gateway at:

- **Endpoint:** ``https://s3.osuosl.org``
- **Region:** any value works; use ``us-east-1`` if your client requires one.

We support **path-style** (``https://s3.osuosl.org/<bucket>``) and
**virtual-hosted** (``https://<bucket>.s3.osuosl.org``) bucket addressing.

.. warning:: Keep your secret key private. Anyone with both keys has full
    access to your buckets. If a key is exposed, contact us so we can rotate it.

s3cmd
-----

`s3cmd <https://s3tools.org/s3cmd>`_ is a simple command-line client. Install it
from your distribution's package manager (``apt install s3cmd``,
``dnf install s3cmd``) or with ``pip install s3cmd``.

Create ``~/.s3cfg`` with your keys:

.. code-block:: ini

    [default]
    access_key = YOUR_ACCESS_KEY
    secret_key = YOUR_SECRET_KEY
    host_base = s3.osuosl.org
    host_bucket = %(bucket)s.s3.osuosl.org
    use_https = True

Then use it:

.. code-block:: console

    $ s3cmd ls                              # list your buckets
    2026-06-10 09:30  s3://fooproject-backups

    $ s3cmd ls s3://fooproject-backups/     # list objects in a bucket
    $ s3cmd put file.tar.gz s3://fooproject-backups/
    $ s3cmd get s3://fooproject-backups/file.tar.gz
    $ s3cmd sync ./localdir/ s3://fooproject-backups/localdir/
    $ s3cmd del s3://fooproject-backups/file.tar.gz

AWS CLI
-------

The `AWS CLI <https://aws.amazon.com/cli/>`_ works against our gateway by
pointing ``--endpoint-url`` at it. Configure a named profile:

.. code-block:: console

    $ aws configure --profile osl
    AWS Access Key ID [None]: YOUR_ACCESS_KEY
    AWS Secret Access Key [None]: YOUR_SECRET_KEY
    Default region name [None]: us-east-1
    Default output format [None]: json

Then pass the endpoint on each command (or set it once with
``AWS_ENDPOINT_URL=https://s3.osuosl.org``):

.. code-block:: console

    $ aws --profile osl --endpoint-url https://s3.osuosl.org s3 ls
    $ aws --profile osl --endpoint-url https://s3.osuosl.org s3 ls s3://fooproject-backups/
    $ aws --profile osl --endpoint-url https://s3.osuosl.org s3 cp file.tar.gz s3://fooproject-backups/
    $ aws --profile osl --endpoint-url https://s3.osuosl.org s3 sync ./localdir/ s3://fooproject-backups/localdir/

rclone
------

`rclone <https://rclone.org/s3/>`_ is handy for syncing and mounting. Add a
remote to ``~/.config/rclone/rclone.conf``:

.. code-block:: ini

    [osl]
    type = s3
    provider = Ceph
    access_key_id = YOUR_ACCESS_KEY
    secret_access_key = YOUR_SECRET_KEY
    endpoint = https://s3.osuosl.org

.. code-block:: console

    $ rclone lsd osl:                                   # list buckets
    $ rclone ls osl:fooproject-backups
    $ rclone copy ./localdir osl:fooproject-backups/localdir
    $ rclone sync ./localdir osl:fooproject-backups/localdir

boto3 (Python)
--------------

To access the service from Python, point `boto3
<https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>`_ at the
endpoint:

.. code-block:: python

    import boto3

    s3 = boto3.client(
        "s3",
        endpoint_url="https://s3.osuosl.org",
        aws_access_key_id="YOUR_ACCESS_KEY",
        aws_secret_access_key="YOUR_SECRET_KEY",
    )

    # Upload, download, and list objects
    s3.upload_file("file.tar.gz", "fooproject-backups", "file.tar.gz")
    s3.download_file("fooproject-backups", "file.tar.gz", "file.tar.gz")

    for obj in s3.list_objects_v2(Bucket="fooproject-backups").get("Contents", []):
        print(obj["Key"], obj["Size"])

Public Access and Listing
-------------------------

By default your bucket is **private**: objects can only be read with your keys,
and the bucket contents cannot be listed anonymously. There are two separate
things you may want to enable:

- **Public read of objects** -- lets anyone download a known object URL such as
  ``https://fooproject-backups.s3.osuosl.org/file.tar.gz``.
- **Public listing** -- lets anyone list the objects in the bucket (the gateway
  returns an XML listing, not a browsable HTML index).

.. warning:: Only make a bucket or object public if the data is meant to be
    available to everyone. Public listing lets anyone enumerate every object in
    the bucket. Never store secrets or private data in a public bucket.

Making objects public with s3cmd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make a single object publicly readable:

.. code-block:: console

    $ s3cmd setacl s3://fooproject-backups/file.tar.gz --acl-public

You can also set the ACL at upload time with ``-P`` / ``--acl-public``:

.. code-block:: console

    $ s3cmd put -P file.tar.gz s3://fooproject-backups/

To make the whole bucket public, including all existing objects, add
``--recursive``:

.. code-block:: console

    $ s3cmd setacl s3://fooproject-backups --acl-public --recursive

To make something private again, use ``--acl-private`` (with ``--recursive`` to
apply it to existing objects).

Enabling public listing with a bucket policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A public ACL on the bucket allows listing, but a bucket policy gives you finer
control and is easier to audit. The following policy makes every object in the
bucket downloadable **and** allows anonymous listing. Save it as
``policy.json``:

.. code-block:: json

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PublicRead",
          "Effect": "Allow",
          "Principal": "*",
          "Action": ["s3:GetObject"],
          "Resource": ["arn:aws:s3:::fooproject-backups/*"]
        },
        {
          "Sid": "PublicList",
          "Effect": "Allow",
          "Principal": "*",
          "Action": ["s3:ListBucket"],
          "Resource": ["arn:aws:s3:::fooproject-backups"]
        }
      ]
    }

Apply it with ``s3cmd``:

.. code-block:: console

    $ s3cmd setpolicy policy.json s3://fooproject-backups

or with the AWS CLI:

.. code-block:: console

    $ aws --profile osl --endpoint-url https://s3.osuosl.org \
        s3api put-bucket-policy --bucket fooproject-backups --policy file://policy.json

If you only want public downloads (a CDN-style bucket where URLs are shared but
the contents aren't enumerable), include just the ``PublicRead`` statement and
omit ``PublicList``.

To remove the policy and make the bucket private again:

.. code-block:: console

    $ s3cmd delpolicy s3://fooproject-backups

A browsable HTML listing
~~~~~~~~~~~~~~~~~~~~~~~~~~

The gateway only returns the raw XML listing described above. If you want a
nice browsable index in a web browser -- like the one the `OpenVox project
<https://yum.overlookinfratech.com/>`_ uses for its package repository -- you
can drop a small single-page app into the bucket that renders the XML listing
client-side. We recommend `aws-s3-bucket-browser
<https://github.com/qoomon/aws-s3-bucket-browser>`_, which is a single
``index.html`` file with no server-side component.

First make sure the bucket allows public listing and downloads, using the
``PublicRead`` + ``PublicList`` bucket policy from the previous section.

Then download ``index.html`` from the project and edit the config block near
the top of the file. The only required setting is ``bucketUrl``, which points at
your bucket's REST endpoint:

.. code-block:: javascript

    const config = {
        title: 'fooproject',
        bucketUrl: 'https://s3.osuosl.org/fooproject-backups',
        // rootPrefix: 'subfolder/',   // only list a subfolder
        // pageSize: 50,
        // defaultOrder: 'name-asc',   // (name|size|dateModified)-(asc|desc)
    }

The page hides its own ``index.html`` from the listing by default, so the
browser file won't show up among your objects.

Upload it to the bucket as a public object:

.. code-block:: console

    $ s3cmd put -P --mime-type=text/html index.html s3://fooproject-backups/

The listing is then available in a browser at the object's URL:

``https://s3.osuosl.org/fooproject-backups/index.html``

Because ``index.html`` is served from the same bucket it lists, the requests are
same-origin and no CORS configuration is needed. If you serve the page from a
different host (for example behind your own domain via ``bucketMaskUrl``), add a
CORS rule allowing ``GET`` from that origin to the bucket.

Notes and Limits
----------------

- **Creating buckets:** We create your project's buckets for you. If you need an
  additional bucket, contact support@osuosl.org rather than creating it
  yourself -- bucket names are shared across the whole gateway and must follow
  the ``<project>-<bucket>`` naming scheme.
- **Object size:** Use multipart uploads for large objects. ``s3cmd``, the AWS
  CLI, and ``rclone`` all do this automatically.
- **Quotas:** We don't normally set quotas, but please be mindful of your usage.
  If you expect to store a large amount of data, let us know in advance.

Getting Help
------------

If you run into trouble, or need a new bucket or a key rotated, email us at
support@osuosl.org.

See Also
--------

- `s3cmd Documentation <https://s3tools.org/s3cmd>`_
- `AWS CLI S3 Reference <https://docs.aws.amazon.com/cli/latest/reference/s3/>`_
- `rclone S3 Documentation <https://rclone.org/s3/>`_
- `Ceph Object Gateway S3 API <https://docs.ceph.com/en/latest/radosgw/s3/>`_
