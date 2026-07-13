def test_admin_user_list(client, admin_header,admin_user):
    response = client.get("/admin/users",headers=admin_header)
    assert response.status_code==200
    
def test_admin_expense_list(client, admin_header,admin_user,user_create_application,admin_create_application):
    response = client.get("/admin/applications",headers=admin_header)
    assert response.status_code == 200


def test_admin_user_delete(client,admin_header):
    response = client.delete("/admin/user/delete/1",headers=admin_header)
    assert response.status_code == 200

def test_admin_application_delete(client,admin_header,user_create_application):
    response = client.delete("/admin/application/delete/1",headers=admin_header)
    assert response.status_code == 200