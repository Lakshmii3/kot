import React from 'react';
import "./Login.css";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';


const LoginLayout = (props) => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-sm">
                </div>
                <div className="col-sm">
                    <Form>
                    <Form.Group controlId="formBasicEmail">
                    <Form.Label>User Name</Form.Label>
                    <Form.Control type="email" placeholder="User Name" />
                    </Form.Group>

                    <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                    </Form.Group>
                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                    </Form>
                </div>
                <div className="col-sm">
                </div>
            </div>
        </div>
    );
}

export default LoginLayout;


