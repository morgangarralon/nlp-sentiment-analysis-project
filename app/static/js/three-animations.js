function onResize(event) {
    camera.aspect = settings.max_width / settings.max_height;
    camera.updateProjectionMatrix();

    renderer.setSize(settings.max_width, settings.max_height);
}

const settings = {
    max_width: 180,
    max_height: 180
}

var speedCloud = .002;
var radiusEarth = 1.5;
var color_negative = 0;
var color_positive = 0; 
var isOpacityUp = true;
var isPositionUp = true;
var guess_result = null;
var scene = new THREE.Scene();
var groupEarth = new THREE.Group();
var selectionables = new THREE.Group();
var textureLoaderCloud = new THREE.TextureLoader();
var renderer = new THREE.WebGLRenderer({ alpha: true });
var ambientLight = new THREE.AmbientLight(0xffffff, .3);
var pointLight = new THREE.DirectionalLight(0xffffff, .5);
var geometryEarth = new THREE.SphereGeometry(radiusEarth, 32, 32);
var directionalLight = new THREE.DirectionalLight(0xffffff, 1, 100);
var earth = new THREE.Mesh(geometryEarth,
            new THREE.MeshPhongMaterial({color: 0x00000, opacity: .05}));
var cloud = new THREE.Mesh(geometryEarth,
            new THREE.MeshPhongMaterial({color: 0x000000, transparent: true}));
var camera = new THREE.PerspectiveCamera(45, settings.max_width / settings.max_height, 0.5, 1000);

textureLoaderCloud.load(window.location.origin + '/static/img/earth_cloud.jpg', function(texture) {
    cloud.material.alphaMap = texture;
    cloud.material.needsUpdate = true;
})
renderer.shadowMap.enabled = true;
scene.background = new THREE.Color(0xffffff)
renderer.setSize(settings.max_width, settings.max_height);
document.getElementById('crystal-ball').appendChild(renderer.domElement);
cloud.scale.setScalar(1.03);
earth.castShadow = true;
groupEarth.add(earth);
groupEarth.add(cloud);
scene.add(groupEarth);
scene.add(ambientLight);
directionalLight.castShadow = true;
directionalLight.position.set(0,.3,0);
scene.add(directionalLight);
pointLight.position.set(0.5,1,0.3);
scene.add(pointLight);
camera.position.z = 8;

var planeGeometry = new THREE.PlaneGeometry(settings.max_width, settings.max_height);
var planeMaterial = new THREE.MeshPhongMaterial({
                    color: 0xffffff, side: THREE.DoubleSide})
var plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.receiveShadow = true;
plane.rotation.x = 80;
plane.position.y = -2.3;
scene.add(plane);
window.addEventListener('resize', onResize);

function animate() {
    // if(earth.material.opacity <= 1 && isOpacityUp) {
    //     earth.material.opacity = earth.material.opacity + .015;
    // } else {
    //     earth.material.opacity = earth.material.opacity - .01;
    //     isOpacityUp = false;

    //     if(earth.material.opacity <= .8) {
    //         isOpacityUp = true;
    //     }
    // }
    if(groupEarth.position.y <= .5 && isPositionUp) {
        groupEarth.position.y = groupEarth.position.y + .015;
    } else {
        groupEarth.position.y = groupEarth.position.y - .01;
        isPositionUp = false;

        if(groupEarth.position.y <= 0) {
            isPositionUp = true;
        }
    }

    if(guess_result == 'negative') {
        earth.material.color = new THREE.Color('rgb(' + color_negative + ',' + color_positive + ', 50)')
        cloud.material.color = new THREE.Color('rgb(' + color_negative + ',' + color_positive + ', 0)')
        if(color_negative <= 230) {
            color_negative +=5
        }
        if(color_positive > 0) {
            color_positive -=5
        }
    } else if(guess_result == 'positive') {
        earth.material.color = new THREE.Color('rgb(' + color_negative + ',' + color_positive + ', 50)')
        cloud.material.color = new THREE.Color('rgb(' + color_negative + ',' + color_positive + ', 0)')
        if(color_positive <= 230) {
            color_positive +=5
        }
        if(color_negative > 0) {
            color_negative -=5
        }
    } else {
        earth.material.color = new THREE.Color('rgb(' + color_negative + ',' + color_positive + ', 50)')
        cloud.material.color = new THREE.Color('rgb(' + color_negative + ',' + color_positive + ', 0)')
        if(color_positive > 0) {
            color_positive -=5
        }
        if(color_negative > 0) {
            color_negative -=5
        }
    }

    cloud.rotateY(speedCloud);
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

animate();