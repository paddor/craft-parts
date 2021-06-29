# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2021 Canonical Ltd.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Source handler definitions and helpers."""

from . import errors  # noqa: F401
from .local_source import LocalSource  # noqa: F401
from .snap_source import SnapSource  # noqa: F401
from .sources import SourceHandler  # noqa: F401
from .sources import get_source_handler  # noqa: F401
from .sources import get_source_type_from_uri  # noqa: F401
