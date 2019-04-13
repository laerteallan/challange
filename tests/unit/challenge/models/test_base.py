
import mock

from challenge.models import BaseModel
from challenge.service import Singleton
from tests import BaseTestClass


class TestBaseModel(BaseTestClass):

    """Class for test the methods module method __init__ models."""

    def setUp(self):
        Singleton.drop()

    @mock.patch("challenge.models.Orm")
    def test_delete_object(self, mock_orm):
        mock_object = mock.MagicMock()
        base = BaseModel()
        base._delete_object(mock_object)
        self.assertTrue(mock_orm().delete_object.called)

    @mock.patch("challenge.models.Orm")
    def test_commit_object(self, mock_orm):
        mock_object = mock.MagicMock()
        base = BaseModel()
        base._commit(mock_object)
        self.assertTrue(mock_orm().object_commit.called)

    @mock.patch("challenge.models.Orm")
    def test_property_session(self, mock_orm):
        base = BaseModel()
        base.session
        self.assertTrue(mock_orm.called)

    @mock.patch("challenge.models.Orm")
    def test_remove_session(self, mock_orm):
        base = BaseModel()
        base.remove_session()
        self.assertTrue(mock_orm().remove_session.called)
