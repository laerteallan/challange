

import mock

from challenge.service import Singleton
from challenge.models.orm import Orm
from tests import BaseTestClass


class TestOrmModel(BaseTestClass):

    """Class for test the methods module method __init__ models."""

    def setUp(self):
        Singleton.drop()

    @mock.patch('challenge.models.orm.create_engine')
    @mock.patch('challenge.models.orm.scoped_session')
    def test_orm(self, mock_scoped_session, mock_create_engine):
        """Test Orm Object."""
        object_fake = mock.MagicMock()
        orm = Orm()
        orm.object_commit(object_fake)
        self.assertTrue(mock_create_engine.called)
        self.assertTrue(mock_scoped_session().add.called)
        self.assertTrue(mock_scoped_session().flush.called)
        self.assertTrue(mock_scoped_session().commit.called)

    @mock.patch('challenge.models.orm.create_engine')
    @mock.patch('challenge.models.orm.scoped_session')
    def test_orm_error(self, mock_scoped_session, mock_create_engine):
        """Test Orm Object."""
        object_fake = mock.MagicMock()
        mock_scoped_session().add.side_effect = Exception("error")
        with self.assertRaises(Exception):
            orm = Orm()
            orm.object_commit(object_fake)
        self.assertTrue(mock_create_engine.called)

    @mock.patch('challenge.models.orm.create_engine')
    @mock.patch('challenge.models.orm.scoped_session')
    def test_orm_commit_error(self, mock_scoped_session, mock_create_engine):
        """Test Orm Object."""
        object_fake = mock.MagicMock()
        mock_scoped_session().flush.side_effect = Exception("error")
        with self.assertRaises(Exception):
            orm = Orm()
            orm.object_commit(object_fake)
        self.assertTrue(mock_create_engine.called)

    @mock.patch('challenge.models.orm.create_engine')
    @mock.patch('challenge.models.orm.scoped_session')
    def test_orm_delete_object(self, mock_scoped_session, mock_create_engine):
        """Test Orm Object."""
        object_fake = mock.MagicMock()
        orm = Orm()
        orm.delete_object(object_fake)
        self.assertTrue(mock_scoped_session().delete.called)
        self.assertTrue(mock_create_engine.called)

    @mock.patch('challenge.models.orm.create_engine')
    @mock.patch('challenge.models.orm.scoped_session')
    def test_remove_session_orm(self, mock_scoped_session, mock_create_engine):
        """Test Base model Object."""
        orm = Orm()
        orm.remove_session()
        self.assertTrue(mock_scoped_session().remove.called)
        self.assertTrue(mock_create_engine.called)

    @mock.patch('challenge.models.orm.create_engine')
    def test_connection_database(self, mock_engine):
        """Test connection database test_connection_database."""
        mock_engine.execute.return_value = True
        orm = Orm()
        orm.test_connection_database()
        self.assertTrue(mock_engine().connect.called)

    @mock.patch('challenge.models.orm.create_engine')
    def test_property_engine(self, mock_engine):
        """Test property engine."""
        mock_engine.execute.return_value = True
        orm = Orm()
        orm.engine
        self.assertTrue(mock_engine.called)
