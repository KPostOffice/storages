#!/usr/bin/env python3
# thoth-storages
# Copyright(C) 2018, 2019 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Exceptions for storage adapters and storage handling."""


class ThothStorageException(Exception):
    """A base exception for Thoth storage exception hierarchy."""


class NotFoundError(ThothStorageException):
    """Raised if the given artifact cannot be found."""


class SchemaError(ThothStorageException):
    """Raised if trying to store document with invalid schema."""


class CacheMiss(ThothStorageException):
    """Raised if the requested document was not found in the cache."""


class NotConnected(ThothStorageException):
    """Raised if there was no connection established when communicating with a storage."""


class MultipleFoundError(ThothStorageException):
    """Raised if there are multiple entities in the graph database when querying for a single one."""


class PythonIndexNotRegistered(ThothStorageException):
    """Raised if an attempt to insert a Python package with an index not being registered to the system."""


class RetryTransaction(ThothStorageException):
    """Raised if number of retries when syncing data into Dgraph exceeded client should retry after some time."""


class UnboundModel(ThothStorageException):
    """Raised if there are done operations on models which do not link to objects stored inside database."""


class PerformanceIndicatorNotRegistered(ThothStorageException):
    """Raised if a performance indicator model which is about to be synced was not found."""


class NotFullyResolved(ThothStorageException):
    """Raised if the transitive query cannot traverse whole dependency graph.

    This means we have not enough dependency related data in the graph database - solvers need to provide them.
    """
