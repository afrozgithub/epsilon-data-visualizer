package io.appium.java_client.android;

import io.appium.java_client.MobileBy;
import io.appium.java_client.MobileElement;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.remote.MobilePlatform;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.io.File;
import java.net.URL;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

/**
 * Test -android uiautomator locator strategy
 */
public class AndroidUIAutomatorTest {

  private AndroidDriver driver;

  @Before
  public void setup() throws Exception {
    File appDir = new File("src/test/java/io/appium/java_client");
    File app = new File(appDir, "ApiDemos-debug.apk");
    DesiredCapabilities capabilities = new DesiredCapabilities();
    capabilities.setCapability(MobileCapabilityType.BROWSER_NAME, "");
    capabilities.setCapability(MobileCapabilityType.DEVICE_NAME, "Android Emulator");
    capabilities.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.ANDROID);
    capabilities.setCapability(MobileCapabilityType.APP, app.getAbsolutePath());
    driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
  }

  @Test
  public void findElementTest() {
    WebElement element = driver.findElementByAndroidUIAutomator("new UiSelector().index(0)");
    assertEquals("android.widget.FrameLayout", element.getTagName());
  }

  @Test
  public void findElementsTest() {
    List<WebElement> elements = driver.findElementsByAndroidUIAutomator("new UiSelector().clickable(true)");
    assertTrue(elements.size() > 11);
  }

  @Test
  public void findElementByTest() {
    WebElement element = driver.findElement(MobileBy.AndroidUIAutomator("new UiSelector().index(0)"));
    assertEquals("android.widget.FrameLayout", element.getTagName());
  }

  @Test
  public void findElementsByTest() {
    List<WebElement> elements = driver.findElements(MobileBy.AndroidUIAutomator("new UiSelector().clickable(true)"));
    assertTrue(elements.size() > 11);
  }

  @Test
  public void findChainedElementsTest() {
	  AndroidElement el1 = (AndroidElement) driver.findElementByAndroidUIAutomator("resourceId(\"android:id/content\")");
	  AndroidElement el2 = (AndroidElement) el1.findElementByAndroidUIAutomator("text(\"Accessibility\")");
	  el2.click();
	  MobileElement el3 = (MobileElement) driver.findElementByAndroidUIAutomator("text(\"Custom View\")");
	  assertTrue(el3.isDisplayed());
  }

  @Test(expected = IllegalArgumentException.class)
  public void ErrorTest() {
    driver.findElementByAndroidUIAutomator(null);
  }

}