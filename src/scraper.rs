use std::{collections::HashMap, rc::Rc, path::Path};

use hyper::{Client, Uri, HeaderMap, body::HttpBody};

const HTML_HEADER: &'static str = "text/html";

#[derive(Debug, Clone)]
struct PageData {
    pub headers: HeaderMap,
    pub body: Vec<u8>,
}

struct Page {
    uri: Uri,
    _data: Option<Rc<PageData>>,
}

impl Page {
    pub async fn data(&mut self) -> Rc<PageData> {
        if let Some(data) = &self._data {
            return Rc::clone(data);
        }

        let client = Client::new();
        let mut response = client.get(self.uri.clone()).await.unwrap();
        
        self._data = Some(Rc::new(PageData {
            headers: response.headers().to_owned(),
            body: response.body_mut().data().await.unwrap().unwrap().to_vec(),
        }));
        
        let rc = self._data.as_ref().unwrap();
        Rc::clone(&rc)
    }

    async fn is_html(&mut self) -> bool {
        let data = self.data().await;

        let resp = data.headers.get("Content-Type").unwrap();
        resp.to_str().unwrap()[..9] == *HTML_HEADER
    }

    async fn save(&mut self, root: Path) {
        
    }
}

#[derive(Debug, Clone, Hash, PartialEq, Eq)]
struct Target(String);
