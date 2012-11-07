Changelog
=========

0.3.2.1 (2012-11-07)
--------------------

- fix brown bag release (docs/ did not get added to the distribution
  by zest.releaser so we added it to MANIFEST.in)
  
0.3.2 (2012-11-06)
------------------

- add the ``zopyx_tinymceplugins_imgmap`` leayer to every
  skin defined in portal_skins on installation to
  prevent people using the product from `getting confused`_
  [fRiSi]

  .. _`getting confused`: http://stackoverflow.com/questions/13227481/overriding-skins-xml-of-another-product


0.3.1 (2011-08-03)
------------------
- added dependency to BeautifulSoup
  [fRiSi]
- added French translation
  [toutpt]

0.3.0 (2010-11-18)
------------------
- added @@getAnchors() view
- added ``Anchors`` fieldset for accessing the list of anchors in the underlaying
  document (works only for ATDocument instance)
  [ajung, d2m]

0.2.0 (2010-10-10)
-------------------
- fixed some packaging issues

0.1.0 (2010-09-27)
-------------------
- Initial release
