# -*- coding: utf-8 -*-
"""Functions related to the documentation.

docdict contains the standard documentation entries
used across SUITPy (source: Nilearn)

source: Eric Larson and MNE-python team.
https://github.com/mne-tools/mne-python/blob/main/mne/utils/docs.py
"""

import sys


###################################
# Standard documentation entries
#
docdict = dict()

NILEARN_LINKS = {"landing_page": "http://nilearn.github.io"}
NILEARN_LINKS["input_output"] = (
    "{}/manipulating_images/input_output.html".format(
        NILEARN_LINKS["landing_page"])
)

# Verbose
verbose = """
verbose : :obj:`int`, optional
    Verbosity level (0 means no message).
    Default={}."""
docdict['verbose'] = verbose.format(1)
docdict['verbose0'] = verbose.format(0)

# Resume
docdict['resume'] = """
resume : :obj:`bool`, optional
    Whether to resume download of a partly-downloaded file.
    Default=True."""

# Data_dir
docdict['data_dir'] = """
data_dir : :obj:`pathlib.Path` or :obj:`str`, optional
    Path where data should be downloaded. By default,
    files are downloaded in home directory."""

# URL
docdict['url'] = """
url : :obj:`str`, optional
    URL of file to download.
    Override download URL. Used for test only (or if you
    setup a mirror of the data).
    Default=None."""

# Smoothing_fwhm
docdict['smoothing_fwhm'] = """
smoothing_fwhm : :obj:`float`, optional.
    If ``smoothing_fwhm`` is not ``None``, it gives
    the full-width at half maximum in millimeters
    of the spatial smoothing to apply to the signal."""

# Standardize
standardize = """
standardize : :obj:`bool`, optional.
    If ``standardize`` is True, the data are centered and normed:
    their mean is put to 0 and their variance is put to 1 in the
    time dimension.
    Default={}."""
docdict['standardize'] = standardize.format('True')
docdict['standardize_false'] = standardize.format('False')

# detrend
docdict['detrend'] = """
detrend : :obj:`bool`, optional
    Whether to detrend signals or not."""

# Target_affine
docdict['target_affine'] = """
target_affine : :class:`numpy.ndarray`, optional.
    If specified, the image is resampled corresponding to this new affine.
    ``target_affine`` can be a 3x3 or a 4x4 matrix.
    Default=None."""

# Target_shape
docdict['target_shape'] = """
target_shape : :obj:`tuple` or :obj:`list`, optional.
    If specified, the image will be resized to match this new shape.
    ``len(target_shape)`` must be equal to 3.

    .. note::
        If ``target_shape`` is specified, a ``target_affine`` of shape
        ``(4, 4)`` must also be given.

    Default=None."""

# Low_pass
docdict['low_pass'] = """
low_pass : :obj:`float` or None, optional
    Low cutoff frequency in Hertz.
    If None, no low-pass filtering will be performed.
    Default=None."""

# High pass
docdict['high_pass'] = """
high_pass : :obj:`float`, optional
    High cutoff frequency in Hertz.
    Default=None."""

# t_r
docdict['t_r'] = """
t_r : :obj:`float` or None, optional
    Repetition time, in seconds (sampling period).
    Set to ``None`` if not provided.
    Default=None."""

# mask_img
docdict['mask_img'] = """
mask_img : Niimg-like object
    Object used for masking the data."""

# Memory
docdict['memory'] = """
memory : instance of :class:`joblib.Memory` or :obj:`str`
    Used to cache the masking process.
    By default, no caching is done. If a :obj:`str` is given, it is the
    path to the caching directory."""

# n_parcels
docdict['n_parcels'] = """
n_parcels : :obj:`int`, optional
    Number of parcels to divide the data into.
    Default=50."""

# random_state
docdict['random_state'] = """
random_state : :obj:`int` or RandomState, optional
    Pseudo-random number generator state used for random sampling."""

# Memory_level
memory_level = """
memory_level : :obj:`int`, optional.
    Rough estimator of the amount of memory used by caching. Higher value
    means more memory for caching.
    Default={}."""
docdict['memory_level'] = memory_level.format(0)
docdict['memory_level1'] = memory_level.format(1)

# n_jobs
n_jobs = """
n_jobs : :obj:`int`, optional.
    The number of CPUs to use to do the computation. -1 means 'all CPUs'.
    Default={}."""
docdict['n_jobs'] = n_jobs.format("1")
docdict['n_jobs_all'] = n_jobs.format("-1")

# img
docdict['img'] = """
img : Niimg-like object
    See `input-output <%(input_output)s>`_.
""" % NILEARN_LINKS

# imgs
docdict['imgs'] = """
imgs : :obj:`list` of Niimg-like objects
    See `input-output <%(input_output)s>`_.
""" % NILEARN_LINKS

# cut_coords
docdict['cut_coords'] = """
cut_coords : None, a :obj:`tuple` of :obj:`float`, or :obj:`int`, optional
    The MNI coordinates of the point where the cut is performed.

        - If ``display_mode`` is 'ortho' or 'tiled', this should
          be a 3-tuple: ``(x, y, z)``
        - For ``display_mode == 'x'``, 'y', or 'z', then these are
          the coordinates of each cut in the corresponding direction.
        - If ``None`` is given, the cuts are calculated automaticaly.
        - If ``display_mode`` is 'mosaic', and the number of cuts is the same
          for all directions, ``cut_coords`` can be specified as an integer.
          It can also be a length 3 tuple specifying the number of cuts for
          every direction if these are different.

        .. note::

            If ``display_mode`` is 'x', 'y' or 'z', ``cut_coords`` can be
            an integer, in which case it specifies the number of
            cuts to perform.

"""

# output_file
docdict['output_file'] = """
output_file : :obj:`str`, or None, optional
    The name of an image file to export the plot to. Valid extensions
    are .png, .pdf, .svg. If ``output_file`` is not None, the plot
    is saved to a file, and the display is closed."""

# extractor / extract_type
docdict['extractor'] = """
extractor : {'local_regions', 'connected_components'}, optional
    This option can take two values:

        - 'connected_components': each component/region in the image is
          extracted automatically by labelling each region based upon the
          presence of unique features in their respective regions.

        - 'local_regions': each component/region is extracted based on
          their maximum peak value to define a seed marker and then using
          random walker segementation algorithm on these markers for region
          separation.

    Default='local_regions'."""
docdict['extract_type'] = docdict['extractor']

# display_mode
docdict['display_mode'] = """
display_mode : {'ortho', 'tiled', 'mosaic','x',\
'y', 'z', 'yx', 'xz', 'yz'}, optional
    Choose the direction of the cuts:

        - 'x': sagittal
        - 'y': coronal
        - 'z': axial
        - 'ortho': three cuts are performed in orthogonal
          directions
        - 'tiled': three cuts are performed and arranged
          in a 2x2 grid
        - 'mosaic': three cuts are performed along
          multiple rows and columns

    Default='ortho'."""

# figure
docdict['figure'] = """
figure : :obj:`int`, or :class:`matplotlib.figure.Figure`, or None,  optional
    Matplotlib figure used or its number. If ``None`` is given, a
    new figure is created."""

# axes
docdict['axes'] = """
axes : :class:`matplotlib.axes.Axes`, or 4 tuple\
of :obj:`float`: (xmin, ymin, width, height), optional
    The axes, or the coordinates, in matplotlib figure
    space, of the axes used to display the plot.
    If ``None``, the complete figure is used."""

# title
docdict['title'] = """
title : :obj:`str`, or None, optional
    The title displayed on the figure.
    Default=None."""

# threshold
docdict['threshold'] = """
threshold : a number, None, or 'auto', optional
    If ``None`` is given, the image is not thresholded.
    If a number is given, it is used to threshold the image:
    values below the threshold (in absolute value) are plotted
    as transparent. If 'auto' is given, the threshold is determined
    magically by analysis of the image.
"""

# annotate
docdict['annotate'] = """
annotate : :obj:`bool`, optional
    If ``annotate`` is ``True``, positions and left/right annotation
    are added to the plot. Default=True."""

# draw_cross
docdict['draw_cross'] = """
draw_cross : :obj:`bool`, optional
    If ``draw_cross`` is ``True``, a cross is drawn on the plot to indicate
    the cut position. Default=True."""

# black_bg
docdict['black_bg'] = """
black_bg : :obj:`bool`, or 'auto', optional
    If ``True``, the background of the image is set to be black.
    If you wish to save figures with a black background, you
    will need to pass facecolor='k', edgecolor='k'
    to :func:`matplotlib.pyplot.savefig`."""

# colorbar
docdict['colorbar'] = """
colorbar : :obj:`bool`, optional
    If ``True``, display a colorbar on the right of the plots."""

# symmetric_cbar
docdict['symmetric_cbar'] = """
symmetric_cbar : :obj:`bool`, or 'auto', optional
    Specifies whether the colorbar should range from ``-vmax`` to ``vmax``
    or from ``vmin`` to ``vmax``. Setting to 'auto' will select the latter
    if the range of the whole image is either positive or negative.

    .. note::

        The colormap will always range from ``-vmax`` to ``vmax``.

"""

# cbar_tick_format
docdict['cbar_tick_format'] = """
cbar_tick_format : :obj:`str`, optional
    Controls how to format the tick labels of the colorbar.
    Ex: use "%%.2g" to display using scientific notation."""

# bg_img
docdict['bg_img'] = """
bg_img : Niimg-like object, optional
    See `input_output <%(input_output)s>`_.
    The background image to plot on top of.
""" % NILEARN_LINKS

# vmin
docdict['vmin'] = """
vmin : :obj:`float`, optional
    Lower bound of the colormap. If ``None``, the min of the image is used.
    Passed to :func:`matplotlib.pyplot.imshow`.
"""

# vmax
docdict['vmax'] = """
vmax : :obj:`float`, optional
    Upper bound of the colormap. If ``None``, the max of the image is used.
    Passed to :func:`matplotlib.pyplot.imshow`.
"""

# bg_vmin
docdict['bg_vmin'] = """
bg_vmin : :obj:`float`, optional
    vmin for ``bg_img``."""

# bg_vmax
docdict['bg_vmax'] = """
bg_vmin : :obj:`float`, optional
    vmax for ``bg_img``."""

# resampling_interpolation
docdict['resampling_interpolation'] = """
resampling_interpolation : :obj:`str`, optional
    Interpolation to use when resampling the image to
    the destination space. Can be:

        - "continuous": use 3rd-order spline interpolation
        - "nearest": use nearest-neighbor mapping.

            .. note::

                "nearest" is faster but can be noisier in some cases.

"""

# cmap
docdict['cmap'] = """
cmap : :class:`matplotlib.colors.Colormap`, or :obj:`str`, optional
    The colormap to use. Either a string which is a name of
    a matplotlib colormap, or a matplotlib colormap object."""

# Dimming factor
docdict['dim'] = """
dim : :obj:`float`, or 'auto', optional
    Dimming factor applied to background image. By default, automatic
    heuristics are applied based upon the background image intensity.
    Accepted float values, where a typical span is between -2 and 2
    (-2 = increase contrast; 2 = decrease contrast), but larger values
    can be used for a more pronounced effect. 0 means no dimming."""

# avg_method
docdict['avg_method'] = """
avg_method : {'mean', 'median', 'min', 'max', custom function}, optional
    How to average vertex values to derive the face value:

        - ``mean``: results in smooth boundaries
        - ``median``: results in sharp boundaries
        - ``min`` or ``max``: for sparse matrices
        - ``custom function``: You can also pass a custom function
          which will be executed though :func:`numpy.apply_along_axis`.
          Here is an example of a custom function:

            .. code-block:: python

                def custom_function(vertices):
                    return vertices[0] * vertices[1] * vertices[2]

"""

# hemi
docdict['hemi'] = """
hemi : {'left', 'right'}, optional
    Hemisphere to display. Default='left'."""

# hemispheres
docdict['hemispheres'] = """
hemispheres : list of :obj:`str`, optional
    Hemispheres to display. Default=['left', 'right']."""

# view
docdict['view'] = """
view : {'lateral', 'medial', 'dorsal', 'ventral',\
        'anterior', 'posterior'}, optional
    View of the surface that is rendered.
    Default='lateral'.
"""

# bg_on_data
docdict['bg_on_data'] = """
bg_on_data : :obj:`bool`, optional
    If ``True``, and a ``bg_map`` is specified,
    the ``surf_data`` data is multiplied by the background
    image, so that e.g. sulcal depth is visible beneath
    the ``surf_data``.

        .. note::
            This non-uniformly changes the surf_data values according
            to e.g the sulcal depth.

"""

# darkness
docdict['darkness'] = """
darkness : :obj:`float` between 0 and 1, optional
    Specifying the darkness of the background image:

        - '1' indicates that the original values of the background are used
        - '.5' indicates that the background values are reduced by half
          before being applied.

"""

# linewidth
docdict['linewidths'] = """
linewidths : :obj:`float`, optional
    Set the boundary thickness of the contours.
    Only reflects when ``view_type=contours``."""

# fsaverage options
docdict['fsaverage_options'] = """

        - 'fsaverage3': the low-resolution fsaverage3 mesh (642 nodes)
        - 'fsaverage4': the low-resolution fsaverage4 mesh (2562 nodes)
        - 'fsaverage5': the low-resolution fsaverage5 mesh (10242 nodes)
        - 'fsaverage5_sphere': the low-resolution fsaverage5 spheres

            .. deprecated:: 0.8.0
                This option has been deprecated and will be removed in v0.9.0.
                fsaverage5 sphere coordinates can now be accessed through
                attributes sphere_{left, right} using mesh='fsaverage5'

        - 'fsaverage6': the medium-resolution fsaverage6 mesh (40962 nodes)
        - 'fsaverage7': same as 'fsaverage'
        - 'fsaverage': the high-resolution fsaverage mesh (163842 nodes)

            .. note::
                The high-resolution fsaverage will result in more computation
                time and memory usage

"""

# Classifiers
base_url = "https://scikit-learn.org/stable/modules/generated/sklearn"
svc = "Linear support vector classifier"
logistic = "Logistic regression"
rc = "Ridge classifier"
dc = "Dummy classifier with stratified strategy"
SKLEARN_LINKS = {
    'svc': f"{base_url}.svm.SVC.html",
    'logistic': f"{base_url}.linear_model.LogisticRegression.html",
    'ridge_classifier': f"{base_url}.linear_model.RidgeClassifierCV.html",
    'dummy_classifier': f"{base_url}.dummy.DummyClassifier.html",
    'ridge': f"{base_url}.linear_model.RidgeCV.html",
    'svr': f"{base_url}.svm.SVR.html",
    'dummy_regressor': f"{base_url}.dummy.DummyRegressor.html",
}

docdict['classifier_options'] = f"""

        - `svc`: `{svc} <%(svc)s>`_ with L2 penalty.
            .. code-block:: python

                svc = LinearSVC(penalty='l2',
                                max_iter=1e4)

        - `svc_l2`: `{svc} <%(svc)s>`_ with L2 penalty.
            .. note::
                Same as option `svc`.

        - `svc_l1`: `{svc} <%(svc)s>`_ with L1 penalty.
            .. code-block:: python

                svc_l1 = LinearSVC(penalty='l1',
                                   dual=False,
                                   max_iter=1e4)

        - `logistic`: `{logistic} <%(logistic)s>`_ with L2 penalty.
            .. code-block:: python

                logistic = LogisticRegression(penalty='l2',
                                              solver='liblinear')

        - `logistic_l1`: `{logistic} <%(logistic)s>`_ with L1 penalty.
            .. code-block:: python

                logistic_l1 = LogisticRegression(penalty='l1',
                                                 solver='liblinear')

        - `logistic_l2`: `{logistic} <%(logistic)s>`_ with L2 penalty
            .. note::
                Same as option `logistic`.

        - `ridge_classifier`: `{rc} <%(ridge_classifier)s>`_.
            .. code-block:: python

                ridge_classifier = RidgeClassifierCV()

        - `dummy_classifier`: `{dc} <%(dummy_classifier)s>`_.
            .. code-block:: python

                dummy = DummyClassifier(strategy='stratified',
                                        random_state=0)

""" % SKLEARN_LINKS

docdict['regressor_options'] = """

        - `ridge`: `Ridge regression <%(ridge)s>`_.
            .. code-block:: python

                ridge = RidgeCV()

        - `ridge_regressor`: `Ridge regression <%(ridge)s>`_.
            .. note::
                Same option as `ridge`.

        - `svr`: `Support vector regression <%(svr)s>`_.
            .. code-block:: python

                svr = SVR(kernel='linear',
                          max_iter=1e4)

        - `dummy_regressor`: `Dummy regressor <%(dummy_regressor)s>`_.
            .. code-block:: python

                dummy = DummyRegressor(strategy='mean')

""" % SKLEARN_LINKS

# mask_strategy
docdict["mask_strategy"] = """
mask_strategy : {'background', 'epi', 'whole-brain-template',\
'gm-template', 'wm-template'}, optional
    The strategy used to compute the mask:

        - 'background': Use this option if your images present
          a clear homogeneous background.
        - 'epi': Use this option if your images are raw EPI images
        - 'whole-brain-template': This will extract the whole-brain
          part of your data by resampling the MNI152 brain mask for
          your data's field of view.

            .. note::
                This option is equivalent to the previous 'template' option
                which is now deprecated.

        - 'gm-template': This will extract the gray matter part of your
          data by resampling the corresponding MNI152 template for your
          data's field of view.

            .. versionadded:: 0.8.1

        - 'wm-template': This will extract the white matter part of your
          data by resampling the corresponding MNI152 template for your
          data's field of view.

            .. versionadded:: 0.8.1

"""

docdict_indented = {}


def _indentcount_lines(lines):
    """Minimum indent for all lines in line list.

    >>> lines = [' one', '  two', '   three']
    >>> _indentcount_lines(lines)
    1
    >>> lines = []
    >>> _indentcount_lines(lines)
    0
    >>> lines = [' one']
    >>> _indentcount_lines(lines)
    1
    >>> _indentcount_lines(['    '])
    0

    """
    indentno = sys.maxsize
    for line in lines:
        stripped = line.lstrip()
        if stripped:
            indentno = min(indentno, len(line) - len(stripped))
    if indentno == sys.maxsize:
        return 0
    return indentno


def fill_doc(f):
    """Fill a docstring with docdict entries.

    Parameters
    ----------
    f : callable
        The function to fill the docstring of. Will be modified in place.

    Returns
    -------
    f : callable
        The function, potentially with an updated ``__doc__``.

    """
    docstring = f.__doc__
    if not docstring:
        return f
    lines = docstring.splitlines()
    # Find the minimum indent of the main docstring, after first line
    if len(lines) < 2:
        icount = 0
    else:
        icount = _indentcount_lines(lines[1:])
    # Insert this indent to dictionary docstrings
    try:
        indented = docdict_indented[icount]
    except KeyError:
        indent = ' ' * icount
        docdict_indented[icount] = indented = {}
        for name, dstr in docdict.items():
            lines = dstr.splitlines()
            try:
                newlines = [lines[0]]
                for line in lines[1:]:
                    newlines.append(indent + line)
                indented[name] = '\n'.join(newlines)
            except IndexError:
                indented[name] = dstr
    try:
        f.__doc__ = docstring % indented
    except (TypeError, ValueError, KeyError) as exp:
        funcname = f.__name__
        funcname = docstring.split('\n')[0] if funcname is None else funcname
        raise RuntimeError('Error documenting %s:\n%s'
                           % (funcname, str(exp)))
    return f
